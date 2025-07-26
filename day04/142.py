# Two Pointers(slow and fast)
# Key Note:
# 1. How to know the length of head to loop enter is equals to the length
# of meeting spot to loop enter(see pic for 142)
# 2. Dont forget return None for the first question.
# 3. Why cant just while fast? because if its an empty Linked List and we call
# fast.next, it would raise an error cause right now fast is None and None cant
# has a next.
# 4. Why slow and fast would meet at the first loop of slow?
# Since the speed difference between slow and fast is 1, so the fast wont 
# jump over slow, it would meets slow once it arrives at slow spot.
# And we can know that during slow's first loop, even though fast is one loop 
# behind slow(which is the extreme circumstances because if its one loop away
# that means they meet), since its speed is twice the slow's, its route would
# cover slow's.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None