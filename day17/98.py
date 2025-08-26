# Validate Binary Search Tree

# Key Note:
# 1. compare two nodes' value to see if its increase(see pic2
# 1-3-5 6-10 11)
# 2. we can set the prev node's value to None or a smallest number
# float('-inf'), we can use smallest number in C++ because
# there maybe the case that the node's value equals to the 
# smallest value.
# 3. we cant just compare the node's left child's value and right
# child's value with it.(see pic3).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.prev = None

    def isValidBST(self, root):
        if root is None:
            return True

        left = self.isValidBST(root.left)

        if self.prev is not None and self.prev.val >= root.val:
            return False
        self.prev = root

        right = self.isValidBST(root.right)
        return left and right
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxVal = float('-inf')
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        left = self.isValidBST(root.left)
        if self.maxVal < root.val:
            self.maxVal = root.val
        else:
            return False
        right = self.isValidBST(root.right)
        return left and right