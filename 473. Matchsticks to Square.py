class Solution:
    def makesquare(self, nums):

        k = 4

        s = sum(nums)
        if s % k != 0:
            return False

        target = s // k
        n = len(nums)

        def dfs(m):

            stack = [(m, 0, {m}, nums[m])]
            while stack:
                # print(stack)
                node, cnt, path, sums = stack.pop()

                if sums == target:
                    if cnt == k - 1:
                        return True
                    for i in range(0, n):
                        if i not in path:
                            stack.append((i, cnt + 1, path | {i}, nums[i]))

                elif sums < target:
                    for i in range(node + 1, n):
                        if i not in path:
                            stack.append((i, cnt, path | {i}, sums + nums[i]))
                else:  # sums > target
                    pass
            return False

        return dfs(0)

ans = Solution()

matchsticks = [1,1,2,2,2]
print(ans.makesquare(matchsticks))
