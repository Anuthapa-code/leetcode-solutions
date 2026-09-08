class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n =  len(nums)
        ans = nums[0]
        maxend = nums[0]
        minend = nums[0]

        for i in range(1 ,n):
            v1 = nums[i]
            v2 = maxend * nums[i]
            v3 = minend * nums[i]

            maxend = max( v1 , v2 , v3)
            minend = min(v1 , v2 , v3)

            ans = max(ans , maxend)
        return ans
