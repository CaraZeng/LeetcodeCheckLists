# Implement Queue using Stacks
# Key Note:
# 1. ## if we dont check if queue is empty or not in thr first place,
# it would raise an error when we call the pop and return.
# 2. return not(self.stack_in or self.stack_out)
# means if any of these two stack has elements, return False
# else, if they are both empty, return True
# or 
# return not self.stack_in or not self.stack_out
# or
# return len(self.stack_in) == 0 and len(self.stack_out) == 0
# it means stacks are empty, if self.stack_in == None, that means
# stack not exists or not been defined
# 3. ## self.empty() so the self is refering to the object who calls pop()
class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        if self.empty(): ##
            return None
        if self.stack_out:
            return self.stack_out.pop() ##
        else:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop() ##

    def peek(self) -> int:
        result = self.pop()
        self.stack_out.append(result)
        return result
        
    def empty(self) -> bool:
        return not(self.stack_in or self.stack_out)