# Sum of Left Leaves (recursion)

# Key Note:
# 1. ## we need the left leaf's value, but if we iterate to that left leaf,
# we dont know the node that this left leaf belongs to has right child or not.
# so we can only iterate to left leaf's parent node and check whether that
# parent node has right child.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 0
        
        leftValue = self.sumOfLeftLeaves(root.left)
        if root.left and not root.left.left and not root.left.right: ##
            leftValue = root.left.val
        rightValue = self.sumOfLeftLeaves(root.right)
        sum_val = leftValue + rightValue
        return sum_val