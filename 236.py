# Lowest Common Ancestor of a Binary Tree

# Key Note:
# 1. There are two different situiations:
# p and q has a common Ancestor
# or
# p is q's Ancestor.
# 2. to get the common Ancestor, we need to traversal from bottom
# to top, so we use post order traversal(backtraking).
# 3. even though we already find the answer, we still need to traversal through
# the whole tree, because we need the whole left and right to return.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == p or root == q or root == None:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left != None and right != None:
            return root
        
        if left == None and right != None:
            return right
        elif left != None and right == None:
            return left
        else:
            return None