class Node:
    # segment tree with lazy propogation for range max query
    # half-open interval [lo, hi)
    def __init__(self, lo, hi, val=0, lazy=0):
        self.lo = lo
        self.hi = hi
        # range max
        self.val = val
        # bookings to add to the children the next time children get visited
        self.lazy = lazy
        self.left = None
        self.right = None


class MyCalendarThree:
    # boundary of calendar range: [LOWER, UPPER)
    LOWER = 0
    UPPER = 1e9 + 1

    def __init__(self):
        self.root = Node(MyCalendarThree.LOWER, MyCalendarThree.UPPER)

    def book(self, start: int, end: int) -> int:
        self.update(self.root, start, end)
        return self.root.val

    def update(self, node, start, end):
        # what happens here is that for each time point in [start, end), bookings + 1
        # we should update all related nodes to maintain the max bookings for [start, end)
        # Time: O(d), where d is the depth of the tree, which is at most log2(1e9)
        # Space: O(n), where n is the number of nodes, or approximately past update calls.

        # range matched
        if node.lo == start and node.hi == end:
            node.val += 1
            node.lazy += 1
            return

        mid = (node.lo + node.hi) // 2

        # push lazy to children
        ## if no children, create them
        if not node.left and not node.right:
            node.left = Node(node.lo, mid, node.lazy, node.lazy)
            node.right = Node(mid, node.hi, node.lazy, node.lazy)
        else:
            node.left.val += node.lazy
            node.left.lazy += node.lazy
            node.right.val += node.lazy
            node.right.lazy += node.lazy
        ## reset lazy
        node.lazy = 0

        # update the children
        if mid >= end:
            self.update(node.left, start, end)
        elif mid <= start:
            self.update(node.right, start, end)
        else:
            self.update(node.left, start, mid)
            self.update(node.right, mid, end)

        # update the node
        node.val = max(node.left.val, node.right.val, node.val)

        return