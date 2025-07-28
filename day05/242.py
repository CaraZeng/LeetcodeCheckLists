# Valid Anagram(using array, defaultdict, counter)
# KeyNote:
# 1.create an array
# 2.use three loops, the big o is o, if we use brute force, the big o
# would be o * o

# Array
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record = [0] * 26

        for i in s:
            record[ord(i) - ord("a")] += 1
        
        for i in t:
            record[ord(i) - ord("a")] -= 1
        
        for i in record:
            if i != 0:
                return False
        return True

# defaultdict
# Key Note:
# ## int tells that the default value is 0
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict

        s_dict = defaultdict(int) ##
        t_dict = defaultdict(int) ##

        for i in s:
            s_dict[i] += 1
        
        for i in t:
            t_dict[i] += 1
        return s_dict == t_dict

# Counter
# Key Note:
# Counter C is capitalized
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        s_counter = Counter(s)
        t_counter = Counter(t)
        return s_counter == t_counter