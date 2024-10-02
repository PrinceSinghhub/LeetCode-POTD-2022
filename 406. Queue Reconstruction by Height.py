class Solution:
    def reconstructQueue(self, people):
        result = []
        for h, k in sorted(people, key=lambda x: (-x[0], x[1])):
            print(k)
            result.insert(k, [h, k])
        return result


ans = Solution()
people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
print(ans.reconstructQueue(people))