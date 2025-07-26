# Remove Nth Node From End of List
# Two pointers(slow and fast)
# Key Note:
# 1. When we move the fast pointer n times, the distance between slow and 
# fast pointer will become n, so when slow and fast move together later, when
# fast reaches None, slow would stay at Nth Node from end of list.
# 2. Since we need to change the Linked List(delete sth), we need to stop
# at the one node that is before the target node. So we can make fast move one
# more step before slow and fast move together, or let condition of 
# fast == None becomes fast.next = None.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, next = head)
        slow = dummy
        fast = dummy
        for i in range(n):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next