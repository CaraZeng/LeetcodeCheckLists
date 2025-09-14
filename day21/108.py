# Convert Sorted Array to Binary Search Tree

# Key Note:
# 1. keep finding mid in the current array and divide it into 
# left and right part then find the mid again and again.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self, nums, left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        root.left = self.traversal(nums, left, mid - 1)
        root.right = self.traversal(nums, mid + 1, right)
        return root
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root = self.traversal(nums, 0, len(nums) - 1)
        return root