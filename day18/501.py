# Find Mode in Binary Search Tree

# Key Note:
# 1. use two pointers(prev and curr) to avoid the second iteration.

# dict(have to iterate the whole tree again to find the max one).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import defaultdict
    def searchBST(self, curr, freq_map):
        if curr == None:
            return
        self.searchBST(curr.left, freq_map)
        freq_map[curr.val] += 1
        self.searchBST(curr.right, freq_map)

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        freq_map = defaultdict(int)
        result = []
        if root == None:
            return result
        self.searchBST(root, freq_map)
        max_freq = max(freq_map.values())
        for key, freq in freq_map.items():
            if freq == max_freq:
                result.append(key)
        return result
    

# use the binary search tree
# use prev and curr
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxCount = 0
        self.count = 0
        self.result = []
        self.prev = None

    def searchBST(self, curr):
        if curr == None:
            return
        
        self.searchBST(curr.left)
        
        if self.prev == None:
            self.count = 1
        elif self.prev.val == curr.val:
            self.count += 1
        else:
            self.count = 1
        self.prev = curr  

        if self.count == self.maxCount:
            self.result.append(curr.val)

        if self.count > self.maxCount:
            self.maxCount = self.count
            self.result = []
            self.result.append(curr.val)

        self.searchBST(curr.right)
        return
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.searchBST(root)
        return self.result

