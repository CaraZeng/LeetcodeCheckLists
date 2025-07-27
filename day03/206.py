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
# 3. Why we dont use dummy and make current = dummy?
# Its not a regular change to Linked List and since dummy = ListNode()
# that means dummy.next = None, and if current == dummy, that means current
# == None
# Here is one mistake i made. And we dont need to consider current.next because eventually
# current would == None and thats ok.
#    dummy = ListNode()           # 创建虚拟头节点
#    pre = dummy                  # pre从虚拟节点开始
#    current = pre.next           # current从虚拟节点的next开始
#    while current and current.next:

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
# Key Note:
# 1. Dont forget the base case curr == None

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