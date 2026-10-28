class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        ans = 0
        sum = 0
        freq = {0:1}

        for i in range(len(nums)):
            sum+=nums[i]
            rem = sum%k

            ans+=freq.get(rem , 0)
            freq[rem] = freq.get(rem , 0)+1
        
        return ans
        