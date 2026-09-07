class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        be = 0
        ans = float("-inf")
         
        for i in range(n):
            v1 = be + nums[i]
            v2 = nums[i]
            be = max(v1 , v2)

            ans = max(ans , be)
        return ans 