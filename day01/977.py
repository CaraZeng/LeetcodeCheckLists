# Two Pointers from start and end to mid
# The value of the numbers' square will be bigger on the left and right side 
# and smaller in the middle, since there -4's square will be 16
# we can create a new List which is the same length, and put the pointer at the 
# last one element. Then we put two pointers at first and last one element in 
# the old list and compare their square. Then we put the bigger one into the new
# List from its end.

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
