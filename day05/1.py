# Two Sum(map, set, two pointer, brute force)
# Key Note:
# 1. When to use hash?
# When we need to look up whether an element appeared before or whether 
# an element is in a set.
# 2. Why we use map here instead of array and set?
# array is for small data, if we got too many values, that will waste space
# set is for only key, to check if it exists.
# map can store both key and value, not only check if it exists but also return
# value
# value can not only be the times an element appears, but also can be its
# index.
# Original data: [5, 5, 6, 6, 7, 7, 7]
# count_map = {
#     5: 2,    # Number 5 appears 2 times
#     6: 2,    # Number 6 appears 2 times  
#     7: 3     # Number 7 appears 3 times
# }
# Original data: [5, 5, 6, 6, 7, 7, 7]
#                0  1  2  3  4  5  6  (indices)
# position_map = {
#     5: [0, 1],       # Number 5 at indices 0 and 1
#     6: [2, 3],       # Number 6 at indices 2 and 3
#     7: [4, 5, 6]     # Number 7 at indices 4, 5, 6
# }
# Only care about existence
# exists_map = {
#     5: True,
#     6: True, 
#     7: True
# }
# In this case, set is more suitable: {5, 6, 7}
# 3. what's map used for?
# To store the elements that we visited before, then when we iterate
# through the nums, we can look up elements in map to combine with num
# to make up the target
# 4. What key and value in map means?
# in this question key is the element and value is the index.


# map
# Key Note:
# 1.dict is map in python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = dict()
        for index, value in enumerate(nums):
            if target - value in record:
                return [record[target - value], index]
            record[value] = index

# set
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [nums.index(complement), i]
            seen.add(num)

# Two Pointers
# Key Note:
# 1. when there are duplicates in array, nums.index will return the first element.
# So if left_index == right _index, its because it return the first element which is
# left_index for right index
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        i = 0
        j = len(nums) - 1
        while i <= j:
            if sorted_nums[i] + sorted_nums[j] == target:
                left_index = nums.index(sorted_nums[i])
                right_index = nums.index(sorted_nums[j])
                if left_index == right_index:
                    right_index = nums[left_index + 1:].index(sorted_nums[j]) + left_index + 1
                return [left_index, right_index]
            elif sorted_nums[i] + sorted_nums[j] < target:
                i += 1
            else:
                j -= 1

# brute force
# Key Note:
# 1. j has to begin from the next to i
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]