# Remove Linked List Elements
# create dummy node for all problems. Because if we want to remove one
# element, we need to make the pointer which point to that element point
# to next element. To do that, we need to know the element in front of that
# element we want to remove. So when the element we want to remove happen to
# be the head node, we need to do extra things to remove head node
# (by making head = head.next).
# Key Note:
# 1.its current.next = current.next.next, because if its 
# current = current.next.next, we would remove current node too.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        current = dummy
        while current and current.next:
            if current.next.val == val:
                current.next = current.next.next ##1
            else:
                current = current.next
            
        return dummy.next

# 创建链表 1->2->6->3->4->5->6
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(6)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next = ListNode(6)

# 调用函数
solution = Solution()
result = solution.removeElements(head, 6)