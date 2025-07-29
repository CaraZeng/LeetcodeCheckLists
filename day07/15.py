# 3Sum
# Two Pointers
# Key Note:
# 1. use i to iterate through the nums and use left and right to find the matches.
# 2. Since we cant contain duplicates, after we append one match to result,
# we need to check if the next num has the same value.
# 3. ## Why we use nums[i] == nums[i - 1] here instead of 
# nums[i] == nums[i + 1]?
# Since left = i + 1, and if in [x, y, z], x == y, is okay. So if we use
# nums[i] == nums[i + 1], we might miss the pairs that nums[i] == nums[left].
class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                return result
            
            if i > 0 and nums[i] == nums[i - 1]: ##
                continue
            
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum_ = nums[i] + nums[left] + nums[right]
                if sum_ < 0:
                    left += 1
                elif sum_ > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result

# dict
# Key Note:
# 1. ## is to make sure that between i and j there are two duplicates and includes
# i that's three numbers in total so we dont need anymore same number so we skip
# the third one.
# 2. ### True stands for mark it that its saved in dict.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                return result
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            d = {}
            for j in range(i + 1, len(nums)):
                if j > i + 2 and nums[j] == nums[j - 1] == nums[j - 2]: ##
                    continue
                c = 0 - nums[i] - nums[j]
                if c in d:
                    result.append([nums[i], nums[j], c])
                    d.pop(c)
                else:
                    d[nums[j]] = True ###
        return result