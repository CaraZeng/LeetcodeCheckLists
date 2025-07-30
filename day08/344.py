# Reverse String
# Key Note:
# 1. If library can just solves the question, dont use it,
# if its just a part of solution, we can use it.
# 2. Changed in place so we dont need to return anything
# Two Pointers while
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

# Two Pointers range
# Key Note:
# 1. dont need to consider if its even or add
# if s == 4, i will stop at 1, and iterate through 2 nums
# is s == 5, i will stop at 1 too. and the middle one acutally dont need
# to move.
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        for i in range(len(s) // 2):
            s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]
