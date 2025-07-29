# 4Sum II
# Key Note:
# 1. Very similar to Two Sum. just calculate the n1 + n2 and see the result
# as one number. And n3 + n4 as one number. Then its a two sum problem.
# 2. ## can be write as hash_map[n1 + n2] = hash_map.get(n1 + n2, 0) + 1

# dict
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hash_map = dict()
        for n1 in nums1:
            for n2 in nums2:
                if n1 + n2 in hash_map:        ##
                    hash_map[n1 + n2] += 1     ##
                else:                          ##
                    hash_map[n1 + n2] = 1      ##
        
        count = 0
        for n3 in nums3:
            for n4 in nums4:
                key = - n3 -n4
                if key in hash_map:
                    count += hash_map[key]
        return count
    
# default dict
# Key Note:
# 1. provide default value
# defaultdict(lambda: 0) has the same function as defaultdict(int)
# means that if you want to visit a value that doesnt exist, it will
# return 0 instead of throw keyerror
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        record = defaultdict(lambda : 0)
        count = 0

        for i in nums1:
            for j in nums2:
                record[i + j] += 1
        for i in nums3:
            for j in nums4:
                count += record.get((- i - j), 0)
        return count
    
'''
The main difference between defaultdict and regular dict is how they 
handle accessing non-existent keys:

1. Accessing Non-existent Keys

Regular dict:
pythond = {}
print(d['key'])  # ❌ KeyError: 'key'

defaultdict:
pythonfrom collections import defaultdict
d = defaultdict(int)
print(d['key'])  # ✅ Returns 0 (default value)

2. Practical Usage Comparison

Counting scenario - Regular dict:
python# Need to check if key exists first
count = {}
words = ['apple', 'banana', 'apple']

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
        
# Or use get method
for word in words:
    count[word] = count.get(word, 0) + 1

Counting scenario - defaultdict:
python# Direct operation, no checking needed
count = defaultdict(int)
words = ['apple', 'banana', 'apple']

for word in words:
    count[word] += 1  # Clean and simple!

3. Different Default Value Types
python# Default value is 0
counter = defaultdict(int)

# Default value is empty list
groups = defaultdict(list)
groups['fruits'].append('apple')  # Automatically creates empty list

# Default value is empty set
sets = defaultdict(set)

# Custom default value
custom = defaultdict(lambda: "unknown")

4. Conversion
python# defaultdict can be used as regular dict
d = defaultdict(int)
d['a'] = 1
regular_dict = dict(d)  # Convert to regular dictionary

# View actual stored key-value pairs
print(dict(d))  # Only shows keys that were actually set

5. Performance
Both have similar performance, but defaultdict leads to cleaner, 
more readable code in scenarios requiring default values by 
eliminating conditional checks.

6. See pic

Bottom line: defaultdict is a "smart" dictionary that knows 
what to return when a key doesn't exist, making code cleaner 
and less error-prone.
'''