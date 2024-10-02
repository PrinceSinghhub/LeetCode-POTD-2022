class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if root:
            if root.val<low:
                return self.rangeSumBST(root.right,low,high)
            elif root.val>high:
                return self.rangeSumBST(root.left,low,high)
            return root.val + self.rangeSumBST(root.left,low,high) + self.rangeSumBST(root.right,low,high)
        else:
            return 0