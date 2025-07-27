# Swap Nodes in Pairs
# Key Note:
# 1. use temp and temp1 to save the two nodes that around the target we need
# to change.
# 2.always current.next then current.next.next. If current.next.next first,
# when current.next is not valid, sth will go wrong.
# 3. Move current to current.next.next at the end of every loop.
# 4. We are switching pairs here, so if its odd, we can left the last one
# along. So if current.next.next is None, we can stop the loop. If its even,
# we can check current.next, and if its None, we can stop the loop. So if either
# of these two happen, we can stop the loop.

# Basic and dummy

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        current = dummy
        while current.next and current.next.next:
            temp = current.next
            temp1 = current.next.next.next
            current.next = current.next.next
            current.next.next = temp
            temp.next = temp1
            current = current.next.next
        return dummy.next

# Recursion
# More Key Note:
# 1. if head == None or head.next == None:
#        return head 
# this is not only the edge cases. because if we call the swapPairs recursively,
# there will always be some new head(next), and we need to check that if there
# any needs to swap again(like only one number or no number left), so is also a base case
# 2. After swap two nodes in on pair, we need to swap the next two nodes, 
# then we can make pre.next the rest of nodes.
# pre.next = self.swapPairs(next)
#  is actually equals to
# result = self.swapPairs(next)
# pre.next = result
# 3. we keep calling swapPairs itself until the end and then end end one call
# returns and the connections happen from the end. And then return happens and
# connection happend.
# 4. In the end we return curr is because after all swaps, the first pair's curr will
# become the first node. swaps happens immediately but connection happens when all 
# swaps are done and connection begins from end to start

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        pre = head
        curr = head.next
        next = curr.next

        curr.next = pre
        pre.next = self.swapPairs(next)
        return curr
'''
# Linked List Swap Pairs Demo: 1->2->3->4->5->6->7

## 📥 Level 1 Call: `swapPairs([1,2,3,4,5,6,7])`

### Before swap:

pre  curr  next(remaining list)
↓    ↓     ↓
1 -> 2 ->  3 -> 4 -> 5 -> 6 -> 7 -> None

### After `curr.next = pre`:

curr -> pre    next(remaining list)
↓       ↓      ↓
2   ->  1      3 -> 4 -> 5 -> 6 -> 7 -> None

---

## 📥 Level 2 Call: `swapPairs([3,4,5,6,7])`

### Before swap:

pre  curr  next(remaining list)
↓    ↓     ↓
3 -> 4 ->  5 -> 6 -> 7 -> None

### After `curr.next = pre`:

curr -> pre    next(remaining list)
↓       ↓      ↓
4   ->  3      5 -> 6 -> 7 -> None

---

## 📥 Level 3 Call: `swapPairs([5,6,7])`

### Before swap:

pre  curr  next(remaining list)
↓    ↓     ↓
5 -> 6 ->  7 -> None

### After `curr.next = pre`:

curr -> pre    next(remaining list)
↓       ↓      ↓
6   ->  5      7 -> None

---

## 📥 Level 4 Call: `swapPairs([7])`

### Single node:

head
↓
7 -> None

**Return 7 directly**

---

## 📤 Recursive Return & Connection Process:

### Level 3 connection: `pre.next = result`, `return curr`

6 -> 5 -> 7 -> None

### Level 2 connection: `pre.next = result`, `return curr`

4 -> 3 -> 6 -> 5 -> 7 -> None

### Level 1 connection: `pre.next = result`, `return curr`

2 -> 1 -> 4 -> 3 -> 6 -> 5 -> 7 -> None

## 🎯 Final Result:

2 -> 1 -> 4 -> 3 -> 6 -> 5 -> 7 -> None

## Recursive Call Stack Summary:
1. `swapPairs([1,2,3,4,5,6,7])` → process(1,2) → return 2
2. `swapPairs([3,4,5,6,7])` → process(3,4) → return 4  
3. `swapPairs([5,6,7])` → process(5,6) → return 6
4. `swapPairs([7])` → single node → return 7

markdown# Recursive Stack Visualization for swapPairs([1,2,3,4,5,6,7])

## 📚 Call Stack (Growing Down)
┌─────────────────────────────────────────────────────────┐
│ swapPairs([1,2,3,4,5,6,7])                             │ ← Main call
│ pre=1, curr=2, next=[3,4,5,6,7]                        │
│ Status: Waiting for recursive result...                 │
├─────────────────────────────────────────────────────────┤
│ swapPairs([3,4,5,6,7])                                 │ ← Called by level 1
│ pre=3, curr=4, next=[5,6,7]                            │
│ Status: Waiting for recursive result...                 │
├─────────────────────────────────────────────────────────┤
│ swapPairs([5,6,7])                                     │ ← Called by level 2
│ pre=5, curr=6, next=[7]                                │
│ Status: Waiting for recursive result...                 │
├─────────────────────────────────────────────────────────┤
│ swapPairs([7])                                         │ ← Called by level 3
│ Base case: single node                                  │
│ Status: Ready to return 7                              │
└─────────────────────────────────────────────────────────┘

## 🔄 Stack Unwinding (Bottom to Top)

### Step 1: Level 4 Returns
┌─────────────────────────────────────────────────────────┐
│ swapPairs([1,2,3,4,5,6,7])                             │
│ Status: Still waiting...                                │
├─────────────────────────────────────────────────────────┤
│ swapPairs([3,4,5,6,7])                                 │
│ Status: Still waiting...                                │
├─────────────────────────────────────────────────────────┤
│ swapPairs([5,6,7])                                     │
│ result = 7  ← Received from recursive call             │
│ pre.next = 7    (5.next = 7)                           │
│ return 6        ← Returns to level 2                   │
├─────────────────────────────────────────────────────────┤
│ ✅ COMPLETED: Returns 7                                 │
└─────────────────────────────────────────────────────────┘

### Step 2: Level 3 Returns
┌─────────────────────────────────────────────────────────┐
│ swapPairs([1,2,3,4,5,6,7])                             │
│ Status: Still waiting...                                │
├─────────────────────────────────────────────────────────┤
│ swapPairs([3,4,5,6,7])                                 │
│ result = 6  ← Received from recursive call             │
│ pre.next = 6    (3.next = 6)                           │
│ return 4        ← Returns to level 1                   │
├─────────────────────────────────────────────────────────┤
│ ✅ COMPLETED: Returns 6 (6->5->7)                       │
├─────────────────────────────────────────────────────────┤
│ ✅ COMPLETED: Returns 7                                 │
└─────────────────────────────────────────────────────────┘

### Step 3: Level 2 Returns
┌─────────────────────────────────────────────────────────┐
│ swapPairs([1,2,3,4,5,6,7])                             │
│ result = 4  ← Received from recursive call             │
│ pre.next = 4    (1.next = 4)                           │
│ return 2        ← Returns to main caller               │
├─────────────────────────────────────────────────────────┤
│ ✅ COMPLETED: Returns 4 (4->3->6->5->7)                 │
├─────────────────────────────────────────────────────────┤
│ ✅ COMPLETED: Returns 6 (6->5->7)                       │
├─────────────────────────────────────────────────────────┤
│ ✅ COMPLETED: Returns 7                                 │
└─────────────────────────────────────────────────────────┘

### Step 4: Level 1 Returns (Final)
┌─────────────────────────────────────────────────────────┐
│ ✅ COMPLETED: Returns 2 (2->1->4->3->6->5->7)           │ ← Final result
├─────────────────────────────────────────────────────────┤
│ ✅ COMPLETED: Returns 4 (4->3->6->5->7)                 │
├─────────────────────────────────────────────────────────┤
│ ✅ COMPLETED: Returns 6 (6->5->7)                       │
├─────────────────────────────────────────────────────────┤
│ ✅ COMPLETED: Returns 7                                 │
└─────────────────────────────────────────────────────────┘

'''