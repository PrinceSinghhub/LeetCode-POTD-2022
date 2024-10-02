class Solution:
    def numsSameConsecDiff(self, n: int, k: int):
        nums = set()
        for d in range(1, 10):
            combs = [[d]]
            for _ in range(1, n):
                next_combs = []
                for comb in combs:
                    if comb[-1] + k < 10:
                        next_combs.append(comb + [comb[-1] + k])
                    if comb[-1] - k > - 1:
                        next_combs.append(comb + [comb[-1] - k])
                combs = next_combs
            nums.update(set(int("".join(map(str, comb))) for comb in combs))
        return list(nums)