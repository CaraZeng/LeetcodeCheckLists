# Top K Frequent Elements(heap and dict)

# heap
# Key Note:
# 1. use map to note down the freq of every elements
# 2. use a pri que(small top) to arrange the elements, so once the lenth
# of pri que is larger than k, we can pop out the smallest element.
# 3. use a list to change the rest heap into list. Since the first element
# in heap is the smallest, we iterate it backwards.
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_ = {}
        for i in range(len(nums)):
            map_[nums[i]] = map_.get(nums[i], 0) + 1

        pri_que = []
        for key, freq in map_.items():
            heapq.heappush(pri_que, (freq, key))
            if len(pri_que) > k:
                heapq.heappop(pri_que)
        
        result = [0] * k
        for i in range(k - 1, -1, -1):
            result[i] = heapq.heappop(pri_que)[1]
        return result

# dict:
# Key Note:
# 1. use a dict to record how many times one element has appeared
# 2. use another dict to save for one appear times, which element
# fits the times.(so its dafaultdict(list) here)
# 3. index.keys() is the times, we turn the times into a list and sort
# the list.
# 4. we create a list to store the result, when key is availble and count
# havent reach k, we append the most freq element in to result
# (index_dict[key[-1]]), and we calcualte how many elements of that freq
# and add it into count.
# 5. After adding them, we pop that freq out of key.
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        time_dict = defaultdict(int)
        for num in nums:
            time_dict[num] += 1
        index_dict = defaultdict(list)
        for key in time_dict:
            index_dict[time_dict[key]].append(key)
        key = list(index_dict.keys())
        key.sort()
        result = []
        count = 0
        while key and count != k:
            result += index_dict[key[-1]]
            count += len(index_dict[key[-1]])
            key.pop()
        return result

