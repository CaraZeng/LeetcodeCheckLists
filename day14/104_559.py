# revisit 104 recursion

# Key Note:
# 1. the difference between height and depth
# for height we should use post order because we count from bottom
# to top
# for depth we should use pre order because we count from top down
# to bottom

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.getDepth(root)
    def getDepth(self, node):
        if not node:
            return 0
        
        leftheight = self.getDepth(node.left)
        rightheight = self.getDepth(node.right)
        height = 1 + max(leftheight, rightheight)
        return height

# 559
# Maximum Depth of N-ary Tree

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        max_depth = 1
        for child in root.children:
            max_depth = max(max_depth, self.maxDepth(child) + 1)
        return max_depth