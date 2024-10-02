class Solution:
    def dfs(self, root, k, aux):
        if not root:
            return False

        if k - root.val in aux:
            return True

        aux.add(root.val)
        l = self.dfs(root.left, k, aux)
        r = self.dfs(root.right, k, aux)
        return l or r

    def findTarget(self, root, k):
        aux = set()
        return self.dfs(root, k, aux)