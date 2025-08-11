# Balanced Binary Tree (recursion)

# Key Note:
# 1. if the height of different subtrees is larger than 1, return False,
# so actually we are calculating the abs difference between the highest subtree
# and second highest subtree(the ultimate bottom).
# 2. firstly we divide the whole tree into left and right subtrees, then
# we divide them into more left and right subtrees, we iterate down the bottom
# of that one tree when root is None, then we return the value from bottom.
# in the process, if any one return -1, that means its not a balanced tree.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.getHeight(root) == -1:
            return False
        else:
            return True
        
    def getHeight(self, root):
        if not root:
            return 0
        
        if (left_height := self.getHeight(root.left)) == -1:
            return -1
        if (right_height := self.getHeight(root.right)) == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        else:
            return 1 + max(left_height, right_height)