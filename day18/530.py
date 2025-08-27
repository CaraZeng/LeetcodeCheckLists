# Minimum Absolute Difference in BST(recursion)

# Key Note:
# 1. Very similar to 98, need to take advantage of the bianry search tree.(inorder traversal
# left mid right so the value will be increase).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = float('inf')
        self.prev = None
    
    def traversal(self, curr):
        if curr == None:
            return
        
        self.traversal(curr.left)
        if self.prev != None:
            self.result = min(self.result, curr.val - self.prev.val)
        self.prev = curr
        self.traversal(curr.right)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.traversal(root)
        return self.result