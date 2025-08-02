# Implement Stack using Queues(one que, two ques)
# Key Note:
# 1. when we want to pop things from stack, we can move all elements
# except the last one into end, and then the last one becomes the first
# one, then we pop it.
# 2. top can be write as
# if self.empty():
#   return None
# return self.que[-1]
# 3. pop can be write as
# if self.empty():
#   return None
# return self.que.pop()

# Use one que
class MyStack:

    def __init__(self):
        self.que = deque()

    def push(self, x: int) -> None:
        self.que.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        for i in range(len(self.que) - 1):
            self.que.append(self.que.popleft())
        return self.que.popleft()

    def top(self) -> int:
        if self.empty():
            return None
        for i in range(len(self.que) - 1):
            self.que.append(self.que.popleft())
        result = self.que.popleft()
        self.que.append(result)
        return result

    def empty(self) -> bool:
        return not len(self.que)
    
# use two ques
# Key Note:
# 1. ## also, this can be write as
# if self.empty():
#     return None
# return self.queue_in[-1] 
class MyStack:

    def __init__(self):
        self.queue_in = deque()
        self.queue_out = deque()

    def push(self, x: int) -> None:
        self.queue_in.append(x)

    def pop(self) -> int: ##
        if self.empty():
            return None
        for i in range(len(self.queue_in) - 1):
            self.queue_out.append(self.queue_in.popleft())
        self.queue_in, self.queue_out = self.queue_out, self.queue_in
        return self.queue_out.popleft()

    def top(self) -> int:
        if self.empty():
            return None

        for i in range(len(self.queue_in) - 1):
            self.queue_out.append(self.queue_in.popleft())
        
        self.queue_in, self.queue_out = self.queue_out, self.queue_in 
        temp = self.queue_out.popleft()   
        self.queue_in.append(temp)
        return temp

    def empty(self) -> bool:
         return len(self.queue_in) == 0
