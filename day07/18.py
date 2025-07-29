# 4Sum
# Key Note:
# 1. a for loop outside 3Sum
# 2. Notice about that ## actually can be omitted
# continue means skip this one, move on to the next one
# break means exit the loop
# return result means just end the function and return
# in this case the return result in i loop can be changed to break
# However, the break in j loop cant be changed to return result
# since maybe just this nums[i] + nums[j] cant work out, it doesnt mean
# the rest of i cant work out.
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > target and nums[i] > 0 and target > 0: ##
                return result ##
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] > target and target > 0: ##
                    break ##
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    sum_ = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum_ > target:
                        right -= 1
                    elif sum_ < target:
                        left += 1
                    else:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
        return result
 
# dict and set
# Key Note:
# 1. use a dict to store the freq for every number, use a set to store the
# result and remove the duplicates
# 2. use three loops to iterate through the possible matches then we can 
# find fourth element. we can calculate the fourth element value, then go
# to the dict to look up whether first three elements has used up all
# freqs. If not, we can add this four matches into ans.
# 3. In ans, we sort the matches first because computer can only see
# the exactly same list as one list.
# For example:
# [1, 1, 2, 3] and [1, 2, 1, 3] is different in computer's perpective,
# but they are duplicates for us. so we need to sort them.
# after sorted, they all become
# [1, 1, 2, 3]
# 4. Since list is change able, so we cant put them into a set(python doesnt
# allowed), so we change them into tuple
# 5. then we put them into set to remove the duplicates.

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        ans = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    val = target - nums[i] - nums[j] - nums[k]
                    if val in freq:
                        count = (nums[i] == val) + (nums[j] == val) + (nums[k] == val)
                        if freq[val] > count:
                            ans.add(tuple(sorted([nums[i], nums[j], nums[k], val])))
        return [list(x) for x in ans]