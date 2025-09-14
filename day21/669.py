# Trim a Binary Search Tree

# Key Note:
# 1. ## is for finding the nodes in between low and high
# 2. ### is for connect the nodes that founded to tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if root == None:
            return None
        if root.val > high: ##
            return self.trimBST(root.left, low, high) ##
        if root.val < low: ##
            return self.trimBST(root.right, low, high) ##
        root.left = self.trimBST(root.left, low, high) ###
        root.right = self.trimBST(root.right, low, high) ###
        return root