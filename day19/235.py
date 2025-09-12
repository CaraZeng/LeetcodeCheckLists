# Lowest Common Ancestor of a Binary Search Tree

# Key Note:
# 1. quite like binary search

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def traversal(self, curr, p, q):
        if curr == None:
            return curr
        if curr.val > p.val and curr.val > q.val:
            left = self.traversal(curr.left, p, q)
            if left:
                return left
        if curr.val < p.val and curr.val < q.val:
            right = self.traversal(curr.right, p, q)
            if right:
                return right
        return curr

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.traversal(root, p, q)