# Reverse Words in a String
# Key Note:
# 1. remove the extra spaces, then reverse the whole s, then reverse
# each part
# 2. dont use erase, because the time complexity of erase is o, and actually
# outside erase we need a loop to iterate through s.
# 3. ## after split, it becomes a list. so we dont need to reverse inside
# each element, because the first reverse only reverses the positions of them
# in the list(treat every element as one object). Instead, if we use reverse
# on s directly, it will just change every letters and spaces.
# 4. ''.join() there wont be spaces between them.
# But ' '.join() will have spcaes between them.
# reverse first then split
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s[::-1]
        s = ' '.join(word[::-1] for word in s.split())
        return s

# split first then reverse ##
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()

        left = 0
        right = len(words) - 1
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1
        return ' '.join(words)

# just use [::-1] ##
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words = words[::-1]
        return ' '.join(words)

# change str into list and use two pointers to remove space
class Solution:
    def singlereverse(self, s, slow, fast):
        while slow < fast:
            s[fast], s[slow] = s[slow], s[fast]
            fast -= 1
            slow += 1
        return s

    def reverseWords(self, s: str) -> str: # s = " hello   world "
        result = ""
        fast = 0
        s = list(s) # [ , h, e, l, l, o,  ,  ,  , w, o, r, l, d, ]
        s.reverse() # [ , d, l, r, o, w,  ,  ,  , o, l, l, e, h, ]
        # remove extra space and put valuable ones into result
        while fast < len(s):
            if s[fast] != " ":
                if len(result) != 0:
                    result += " "
                while fast < len(s) and s[fast] != " ":
                    result += s[fast]
                    fast += 1
            else:
                fast += 1 
        # result = "dlrow olleh"
        
        # reverse every word
        slow = 0
        fast = 0
        result = list(result) # result = [d, l, r, o, w,  , o, l, l, e, h]
        while fast <= len(result):
            if fast == len(result) or result[fast] == " ":
                self.singlereverse(result, slow, fast - 1)
                slow = fast + 1
            fast += 1
        # result = [w, o, r, l, d,  , h, e, l, l, o]
        
        return "".join(result)

# Once we meet an space, that means there is a word before.
# Key Note:
# 1. why if word != '': not if word != ' ':
# because if char == ' ': we start to consider and append
# so if is not ' ', we add to word. so word will never has a ' '
# and never be a ' '
class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        word = ''
        s += ' '

        for char in s:
            if char == ' ':
                if word != '':
                    words.append(word)
                    word = ''
                continue
            word += char
        
        words.reverse()
        return ' '.join(words)
