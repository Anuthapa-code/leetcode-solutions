class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        n = len(nums)
        arr = nums.copy()
        total = 0

        for i in range(n):
            total += nums[i]
            arr[i] = total

        return arr