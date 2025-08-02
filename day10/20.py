# Valid Parentheses
# Key Note:
# 1. first iterate through left parentheses items in s, and add the 
# corresboding right parentheses in stack.
# When item not euqals to any of these three left parentheses, it
# means we now arrive at right part of s.
# stack[-1] means the first item in the exit, so if it not euqals to
# the first on the right part(corresboding to the last one in the left
# part), or stack is not available(it means that we dont have enough
# right part items to pop out), we return False
# if everything going ok, we pop out the corresding items from stack,
# in the end if the stack is empty we return True, if its not, it means
# that we dont have enough right part items, so we got extra left part,
# and we return False.
# 2. In a word, there are three situiations to return false,
# first is extra left, second is extra right, third is not coresboding.

# stack
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for item in s:
            if item == '(':
                stack.append(')')
            elif item == '{':
                stack.append('}')
            elif item == '[':
                stack.append(']')
            elif not stack or stack[-1] != item:
                return False
            else:
                stack.pop()
        return True if not stack else False
    
# dict
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        for item in s:
            if item in mapping.keys():
                stack.append(mapping[item])
            elif not stack or stack[-1] != item:
                return False
            else:
                stack.pop()
        return True if not stack else False