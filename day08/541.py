# Recerse String II
# Key Note:
# 1. divide s into multiple parts which length is k, then reverse every
# other part.
# 2. ## text is just a varaible's name
class Solution:
    def reverse(self, text): ##
        left = 0
        right = len(text) - 1
        while left < right:
            text[left], text[right] = text[right], text[left]
            left += 1
            right -= 1
        return text

    def reverseStr(self, s: str, k: int) -> str:
        res = list(s)

        for curr in range(0, len(s), 2 * k):
            res[curr: curr + k] = self.reverse(res[curr: curr + k])
        return ''.join(res)
    
# Two pointers
# Key Note:
# 1. [::-1] means reverse
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        p = 0
        while p < len(s):
            p2 = p + k
            s = s[:p] + s[p: p2][::-1] + s[p2:]
            p += 2 * k
        return s
    
# Just use [::-1]
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i = 0
        chars = list(s)

        while i < len(s):
            chars[i : i + k] = chars[i : i + k][::-1]
            i += 2 * k
        return ''.join(chars)