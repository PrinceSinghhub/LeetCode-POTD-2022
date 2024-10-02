"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head):
        if head is None: return None
        mapping = {}
        cur = head
        while cur:
            mapping[cur] = Node(cur.val,None,None)
            cur = cur.next
        cur = head
        while cur:
            if cur.next:
                mapping[cur].next = mapping[cur.next]
            if cur.random:
                mapping[cur].random = mapping[cur.random]
            cur = cur.next
        return mapping[head]


ans = Solution()
head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
print(ans.copyRandomList(head))