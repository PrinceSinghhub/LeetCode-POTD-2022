class Solution:
    def minDominoRotations(self, A, B):
        n = len(A)
        cnt = [0] * 6
        a_cnt = [0] * 6
        b_cnt = [0] * 6
        for a, b in zip(A, B):
            if a != b:
                cnt[b - 1] += 1
            b_cnt[b - 1] += 1
            cnt[a - 1] += 1
            a_cnt[a - 1] += 1
        ans = n
        for i, val in enumerate(cnt):
            if val >= n:
                ans = min(ans, n - a_cnt[i], n - b_cnt[i])
        return ans if ans != n else -1


ans = Solution()
tops = [2,1,2,4,2,2]
bottoms = [5,2,6,2,3,2]
print(ans.minDominoRotations(tops,bottoms))
