# Maximum Binary Tree (recursion)

# similar to 106_105

# Key Note:
# 1. as long as construct binary tree, use PREORDER TRAVERSAL
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        root_val = max(nums)
        root = TreeNode(root_val)

        separator_idx = nums.index(root_val)

        left = nums[:separator_idx]
        right = nums[separator_idx + 1:]

        root.left = self.constructMaximumBinaryTree(left)
        root.right = self.constructMaximumBinaryTree(right)
        return root