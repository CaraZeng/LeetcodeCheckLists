# Sliding Window Maximum
# Key Note:
# 1. define a queue by oursleves. There are no such enter and exit of
# this queue. only the head(0) and tail(-1)
# pop out head when value is == head
# pop out tail when value is > tail then append value to tail.
# make sure the head is max and tail is min and queue is Monotonic.
# every time we can return the max(head of queue) and save it to result.
# 2. Why we need Monotonic Queue and return the front, not just use
# get max?
# get max actually will use for loop.
from collections import deque

class MyQueue:
    def __init__(self):
        self.queue = deque()
    
    def pop(self, value):
        if self.queue and value == self.queue[0]: # pop(nums[i - k]) when move 
            self.queue.popleft()                  # forward

    def push(self, value):
        while self.queue and value > self.queue[-1]: # remove the numbers that
            self.queue.pop()                         # are smaller then the new number
        self.queue.append(value)                     # because we dont need them
    
    def front(self):
        return self.queue[0]

# nums[1, 3, -1, -3, 5, 3, 6, 7] k = 3
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = MyQueue()
        result = []
        for i in range(k):
            queue.push(nums[i]) # queue = [3, -1]
        result.append(queue.front()) # result = [3]
        for i in range(k, len(nums)): # i = 7 queue = [7]
            queue.pop(nums[i - k]) # i - k = 4
            queue.push(nums[i])
            result.append(queue.front()) # result = [3, 3, 5, 5, 6, 7]
        return result