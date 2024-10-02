class NumArray:

    def __init__(self, nums):
        self.nums = nums
        self.sums = sum(nums)

    def update(self, index, val):
        self.sums += val - self.nums[index]
        self.nums[index] = val

    def sumRange(self, left, right):
        if right - left < len(self.nums) // 2:
            return sum(self.nums[left:right + 1])
        else:
            return self.sums - sum(self.nums[:left]) - sum(self.nums[right + 1:])

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)