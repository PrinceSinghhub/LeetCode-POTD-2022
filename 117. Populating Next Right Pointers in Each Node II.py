class Solution:

    def connect(self, root):
        dic = dict()

        def helper(root, level):
            if not root:
                return
            if level in dic:
                dic[level].next = root
                dic[level] = root
            else:
                dic[level] = root
            helper(root.left, level + 1)
            helper(root.right, level + 1)
            return

        helper(root, 0)
        return root