class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        node = arr[0]
        onedel = float("-inf")
       
        prevnode = node
        prevonedel = onedel

        res = node

        for i in range(1 , n):

            node = max(prevnode+arr[i] , arr[i])

            onedel = max(prevnode , prevonedel+arr[i])

            res = max(res , node , onedel)

            prevnode = node
            prevonedel = onedel

        return res
        