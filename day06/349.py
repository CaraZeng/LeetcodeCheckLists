# Intersection of Two Arrays (set and array)
# If data is big, use set, if data is small, use array, if its small
# but sparse, use set.

# Key Note:
# 1. dict.get(key, default)
# 2. since we need to return list contains unique elements. so we use 
# set here because it only contains first one of each unique elements.
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        table = {}
        for num in nums1:
            table[num] = table.get(num, 0) + 1
        
        res = set()
        for num in nums2:
            if num in table:
                res.add(num) ##
                table[num] -= 1
        return list(res)

# Array
# Key Note:
# 1. use index to be key, use two arrays to store how many times are
# different elements appear. Then compares two arrays, if the multiply
# of the same index in two different arrays are > 0(that means they are 
# all at least 1), then we can select that element to result.
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = [0] * 1001
        count2 = [0] * 1001
        result = []

        for i in range(len(nums1)):
            count1[nums1[i]] += 1
        for j in range(len(nums2)):
            count2[nums2[j]] += 1
        
        for k in range(1001):
            if count1[k] * count2[k] > 0:
                result.append(k)
        return result 
    
# Set
# Key Note:
# 1. set() is to make nums array becomes set(which contains unique element)
# 2. & is the intersection
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))