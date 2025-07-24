# Sliding Window (Two Pointers)
# the end pointer is always move one step, but when necessary, we need to
# move start point to narrow down the window as much as possible.
# Key note: 
# 1. if we want to know the minimal value, we should set the init
# value to be float('inf), if we want the max value, we should set the init
# value to be float('-inf')
# 2.we should save the result first every time before we narrow down the window,
# because there is the chance that once we narrow down it, it doesnt meet the
# condition anymore (while s >= target).
# 3.since in this case, we keep move end point, so we can use for loop here.

# Brute Force
# It failed in Leetcode because of Time Limited
# Key Note:
# 1. s = 0 is inside of first for loop because we try to find every possible length
# for every possible start point.
# 2. Once we find the s that meet the condition, we break the code. Because now we
# are calculating every possibilities, so we are trying to calculate every j point
# with a fixed i point. So the first point where s meets the condition will causes
# the smallest s. What we need to do is note down every smallest result for different
# start point, then return the smallest one among them.
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = float('inf')
        for i in range(len(nums)):
            s = 0
            for j in range(i, len(nums)):
                s += nums[j]
                if s >= target:
                    result = min(result, j - i + 1)
                    break
        return result if result != float('inf') else 0
    
# Sliding Window

# For loop
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i ,j = 0, 0
        result = float('inf')
        s = 0
        for j in range(len(nums)): ##
            s += nums[j]
            while s >= target:
                result = min(result, j - i + 1)
                s -= nums[i]
                i += 1
            ##
        return result if result != float('inf') else 0

# While loop
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i ,j = 0, 0
        result = float('inf')
        s = 0
        while j < len(nums): ##
            s += nums[j]
            while s >= target:
                result = min(result, j - i + 1)
                s -= nums[i]
                i += 1
            j += 1 ##
        return result if result != float('inf') else 0
    

