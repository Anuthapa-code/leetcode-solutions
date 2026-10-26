class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        res = 0
        freq = {}
        freq[0] = 1

        for i in range(len(nums)):
            curr_sum += nums[i]

            ques = curr_sum - k
            res += freq.get(ques ,0)

            freq[curr_sum] = freq.get(curr_sum , 0) + 1

        return res

        