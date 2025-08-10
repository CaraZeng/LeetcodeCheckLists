# Symmetric Tree

# Key Note:
# 1. when do we need post order, not pre order and inorder?
# when we need to gather the information of left and right child and
# return it to their parent. basically this problem is solved by 
# iterate down the bottom then compare the last one from ouside line,
# and last one from inside line, and return result to their own mid.
# ## we iterate left part and right part by left right mid or right left mid
# for each part.(one left right mid then the other one is right left mid)
# so that we can deal outside and inside for each one.
# 2. we 
# return inside and outside
# instead of
# return inside == outside
# because compare returns bool, if inside and outside both
# be false, and we use ==, it can be true.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.compare(root.left, root.right)   
    def compare(self, left, right):
        if left == None and right != None:
            return False
        elif left != None and right == None:
            return False
        elif left == None and right == None:
            return True
        elif left.val != right.val:
            return False
        outside = self.compare(left.left, right.right) ##
        inside = self.compare(left.right, right.left)  ##
        return inside and outside

# 100
# Same Tree
# very similar to 101

# Key Note:
# 1. we 
# return left_part and right_part
# instead of
# return left_part == right_part
# because compare returns bool, if left_part and right_part both
# be false, and we use ==, it can be true.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.compare(p, q)
    
    def compare(self, p, q):
        if p == None and q != None:
            return False
        elif p != None and q == None:
            return False
        elif p == None and q == None:
            return True
        elif p.val != q.val:
            return False
        
        left_part = self.compare(p.left, q.left)
        right_part = self.compare(p.right, q.right)
        return left_part and right_part

# 572

# Subtree of Another Tree
# Key Note:
# 1. similar to 101 and 100.
# just compare part of the tree to subRoot.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
        
        return(self.isSameTree(root, subRoot) or
                self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot)
        )
    
    def isSameTree(self, p, q):
        if p and not q:
            return False
        elif not p and q:
            return False
        elif not p and not q:
            return True
        elif p.val != q.val:
            return False
        
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        return left and right