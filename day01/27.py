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