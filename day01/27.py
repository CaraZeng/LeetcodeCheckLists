# Two loops
# One is used to track the numbers and check if it is equals to val
# Second is used to cover the number that equals to val by its next number
# After it, the index of first loop should go back one step because we delete a number
# Brute Force
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, size = 0, len(nums)

        while i < size:
            if nums[i] == val:
                for j in range(i + 1, size):
                    nums[j - 1] = nums[j]
                i -= 1
                size -= 1
            i += 1
        return size

# Two Pointers(slow and fast)
# The fast pointer is used to check whether the number is equals to val
# The slow pointer is used to save the number that is not equals to val
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, 0
        size = len(nums)
        while j < size:
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i