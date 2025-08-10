# 111 Minimum Depth of Binary Tree

# Key Note:
# 1. what's leaf node?
# if a node's left node and right node both are None, its a leaf
# node.
# 2. and the minimum depth is the distance from root node to nearest
# leaf node, so dont mess up with a node that contains a node with None
# but not with two Nones.
# see pic
# 3. so even though we only calculate the left and right subtree of the
# first node, and left and right subtree becomes more left and right
# subtree later. However, those left and right subtree will go all the
# way down to bottom and post order iterate from bottom and return
# to the top, so that we know the height of left and right subtree of
# first node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.getDepth(root)
    def getDepth(self, root):
        if not root:
            return 0
        
        leftDepth = self.getDepth(root.left)
        rightDepth = self.getDepth(root.right)
    
        if root.left is None and root.right:
            return 1 + rightDepth
        elif root.left and root.right is None:
            return 1 + leftDepth
        
        result = 1 + min(leftDepth, rightDepth)
        return result