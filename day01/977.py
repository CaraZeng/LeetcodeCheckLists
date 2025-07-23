# Two Pointers from start and end to mid
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        new_nums = len(nums) * [0]
        k = len(nums) - 1
        while i <= j:
            if nums[i] * nums[i] >= nums[j] * nums[j]:
                new_nums[k] = nums[i] * nums[i]
                i += 1
            else:
                new_nums[k] = nums[j] * nums[j]
                j -= 1
            k -= 1
        return new_nums
