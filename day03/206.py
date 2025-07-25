# Reverse Linked List
# Key Note:
# 1. use a temp to save the curr.next, then make curr.next = pre to reverse
# the direction, the move pre to curr first because if we move curr to temp
# first we would lost current so pre has nowhere to go.
# 2. Why we always need a pre before current?
# First is that we need to make current point to old current, so pre is used
# to save old current
# Second is that when we at the first current, since the end of Linked List
# is None, and we need to reverse the Linked List, so we need pre to be the 
# None.

# Two Pointers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = pre
            pre = curr
            curr = temp
        return pre
    
# Recursion

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverse(head, None)
    def reverse(self, curr: ListNode, pre: ListNode) -> ListNode:
        if curr == None:
            return pre
        temp = curr.next
        curr.next = pre
        return self.reverse(temp, curr)