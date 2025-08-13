# Count Complete Tree Nodes (recursion)
# can solved by regular binary tree
# also can be solved base on its Complete Binary Tree

# Complete Binary Tree
# Key Note:
# 1. see pic, and because its a complete binary tree, we can calcuate
# the number of nodes by knowing the left height and right height.
# complete either be full binary tree or not full in the bottom but all
# nodes are as left as possible.
# if its full, we can calculate it, if its not full, as long as we keep
# iterate it, we will definitely reach a full subtree when we need to 
# stop, no matter how large it is 
# or 
# its just a node(its also full binary tree), so we can apply
# the solution(calculate based on left depth and right depth) to every 
# full subtree.
# 2. 2 << left_depth
# ==
# 2 * 2**1

# Complete binary tree solution:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = root.left
        right = root.right
        left_depth = 0
        right_depth = 0

        while left:
            left = left.left
            left_depth += 1
        while right:
            right = right.right
            right_depth += 1
        if left_depth == right_depth:
            return (2 << left_depth) - 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
    
# regular binary tree solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        return self.getNodesNum(root)
    def getNodesNum(self, root):
        if not root:
            return 0
        
        left_nodes = self.getNodesNum(root.left)
        right_nodes = self.getNodesNum(root.right)
        tree_nodes = left_nodes + right_nodes + 1
        return tree_nodes