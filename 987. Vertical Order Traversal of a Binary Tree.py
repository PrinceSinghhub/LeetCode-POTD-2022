# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque


class Solution:

    def leveOrderTraversal(self, myans, root):

        if not root:
            return

        queue = deque()
        queue.append([root, 0, 0])

        while len(queue) != 0:

            data = queue.popleft()
            Node = data[0]
            VarticalNumber = data[1]
            levelNumber = data[2]

            myans[VarticalNumber].append((levelNumber, Node.val))

            if Node.left:
                queue.append([Node.left, VarticalNumber - 1, levelNumber + 1])

            if Node.right:
                queue.append([Node.right, VarticalNumber + 1, levelNumber + 1])

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        myans = defaultdict(list)

        self.leveOrderTraversal(myans, root)

        print(myans)

        varticals = list(myans.keys())
        varticals.sort()
        print(varticals)

        ans = []
        for i in varticals:
            temp = []
            for val in sorted(myans[i]):
                temp.append(val[1])

            ans.append(temp)

        print(ans)
        return ans






