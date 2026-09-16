class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n = len(nums)
        max_prev = 0
        min_prev = 0
        res = 0

        for i in range(n):
            max_v1 = max_prev+nums[i]
            max_v2 = nums[i]

            min_v1 = min_prev + nums[i]
            min_v2 = nums[i]

            max_prev = max(max_v1,max_v2)
            min_prev = min(min_v1,min_v2)

            res = max(res , abs(max_prev),abs(min_prev))

        return res