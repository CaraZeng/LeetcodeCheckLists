# Binary Tree Paths (recursion)

# Key Note:
# 1. basically this problem is we append node'value into path, and if the
# node has left or right node, we traversally explore the left and right node,
# after calling the traversal functions, we need to backtrack because
# we got other paths to explore. in every traversal, if that node has
# nothing to explore next, we return that traversal. we dont need to
# return anything for a traversal because we are just append things to
# result.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = [] # result = []
        path = [] # path = []
        if not root:
            return result
        self.traversal(root, path, result)
        return result
    
    def traversal(self, curr, path, result):
        path.append(curr.val) ## excute
        if not curr.left and not curr.right: ###
            sPath = '->'.join(map(str, path)) ###
            result.append(sPath) ###
            return ### base case
        if curr.left: 
            self.traversal(curr.left, path, result) ### recursive
            path.pop() #### backtrack
        if curr.right:
            self.traversal(curr.right, path, result) ###recursive
            path.pop() #### backtrack