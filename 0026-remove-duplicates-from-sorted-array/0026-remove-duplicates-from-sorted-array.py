class Solution:
    def removeDuplicates(self, nums ):
        if not nums:
            return 0

        officer = 0
        
        for cm in range(1 , len(nums)):
            if(nums[officer]!=nums[cm]):
                officer+=1
                nums[officer]=nums[cm]

        return officer+1

                
        
        