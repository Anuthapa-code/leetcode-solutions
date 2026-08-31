class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def next_ind(i):
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue

            slow = i
            fast = i
            d = nums[i] > 0

            while True:
                if nums[slow] == 0 or (nums[slow] > 0) != d:
                    break
                if nums[fast] == 0 or (nums[fast] > 0) != d:
                    break

                slow = next_ind(slow)

                next_fast = next_ind(fast)
                if nums[next_fast] == 0 or (nums[next_fast] > 0) != d:
                    break
                fast = next_ind(next_fast)

                if slow == fast:
                    if slow == next_ind(slow):  # single element loop
                        break
                    return True

            # ✅ mark visited loop should be OUTSIDE while, not after return
            j = i
            while nums[j] != 0 and (nums[j] > 0) == d:
                next_j = next_ind(j)
                nums[j] = 0
                j = next_j

        return False   # ✅ ye for loop ke baad hona chahiye
