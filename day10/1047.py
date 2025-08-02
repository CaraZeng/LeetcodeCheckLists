# Remove All Adjacent Duplicates In String

# stack
class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = list()
        for item in s:
            if res and res[-1] == item:
                res.pop()
            else:
                res.append(item)
        
        return ''.join(res)


# My solution
# Key Note:
# 1. ## its left closed right open, so if we want to include 1, we 
# have to start from 1
# 2. in python, we use list to perform stack. and we use different
# functions (pop for stack) to distinguish them.
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        s = list(s)
        stack.append(s[0])
        for item in s[1: ]: ##
            stack.append(item)
            if 2 <= len(stack) and stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
        
        return ''.join(stack)

# Two pointer to simulate stack
class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = list(s)
        slow = fast = 0
        length = len(res)

        while fast < length:
            res[slow] = res[fast]
            if slow > 0 and res[slow] == res[slow - 1]:
                slow -= 1
            else:
                slow += 1
            fast += 1
        return ''.join(res[0: slow])
