class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        res= float("inf")
        high = 0
        low = 0
        sum = 0

        for high in range(n):
            sum += nums[high]
            while sum >= target:
                length = high-low+1
                res = min(res , length)
                sum -= nums[low]
                low+=1

        
        return 0 if res == float("inf")else res

            
        