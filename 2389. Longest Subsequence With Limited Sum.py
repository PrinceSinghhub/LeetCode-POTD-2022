class Solution:
    def answerQueries(self, nums, queries):
        nums.sort()
        arr = []
        for query in queries:
            count, sm = 0, 0
            for i in range(len(nums)):
                if sm + nums[i] <= query:
                    sm += nums[i]
                    count += 1
            arr.append(count)
        return arr