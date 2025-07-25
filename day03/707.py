# Design Linked List
# Key Note:
# 1. Need to create a ListNode class because we need to draw the linked List
# by ourselves.
# 2. need a size
# 3. How to determind whether current = dummy or current = dummy.next?
# If we want to look up sth, we need to start from the first valid node, which
# is the one after dummy. If we want to make a change, we need the one node
# that is before the node we need to change to make a change. So we start
# from the dummy node.
# 4. when current = dummy.next, after for i in range(index), we will at
# index
# when current = dummy, after for i in range(index), we will at the one 
# before index
# even though the for loop wont iterate till index, but we start from 0, so
# actually there would be index-number loops.
# 5. For the get function, if the index is not valid, we need to return -1
# But for the addAtIndex, if the index < 0, it is add at head, so its valid
# If index = size, its add at tail, it valid too.
# For deleteAtIndex, if the index is not valid, just return
# 6. For addAtTail, since we dont know there are how many nodex, we can use while to move current until current.next is 
# not valid.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.dummy = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        current = self.dummy.next
        for i in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        self.dummy.next = ListNode(val, self.dummy.next)
        self.size += 1

    def addAtTail(self, val: int) -> None:
        current = self.dummy
        while current.next:
            current = current.next
        current.next = ListNode(val, None)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        current = self.dummy
        for i in range(index):
            current = current.next
        current.next = ListNode(val, current.next)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        current = self.dummy
        for i in range(index):
            current = current.next
        current.next = current.next.next
        self.size -= 1