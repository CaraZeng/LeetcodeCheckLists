# 112 Path Sum

# Key Note:
# 1. return True is the traversal is True, because we need to pass the 
# boolean up.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self, curr, count):
        if not curr.left and not curr.right and count == 0:
            return True
        if not curr.left and not curr.right:
            return False
        
        if curr.left:
            count -= curr.left.val
            if self.traversal(curr.left, count):
                return True
            count += curr.left.val
        
        if curr.right:
            count -= curr.right.val
            if self.traversal(curr.right, count):
                return True
            count += curr.right.val
        return False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return self.traversal(root, targetSum - root.val)

# 113

# Key Note:
# 1. since result and path is shared by two functions, and we need
# to reset path every time after we append path to result. so we 
# use __init__, actually we dont need __init__ for result because we 
# only use result one time, but for the elegance of our code, we put
# result into __init__ too.
# 2. ## actually these two lines can switch positions because they dont interfere
# with each other
# 3. self.path[:]
# means the whole path.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = []
        self.path = []

    def traversal(self, curr, count):
        if not curr.left and not curr.right and count == 0:
            self.result.append(self.path[:]) ###
            return
        if not curr.left and not curr.right:
            return
        
        if curr.left:
            self.path.append(curr.left.val)
            count -= curr.left.val
            self.traversal(curr.left, count)
            count += curr.left.val ##
            self.path.pop() ##
        if curr.right:
            self.path.append(curr.right.val)
            count -= curr.right.val
            self.traversal(curr.right, count)
            count += curr.right.val ##
            self.path.pop() ##
        return
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.result.clear()
        self.path.clear()
        if not root:
            return self.result
        self.path.append(root.val)
        self.traversal(root, targetSum - root.val)
        return self.result

        