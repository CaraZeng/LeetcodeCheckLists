# Delete Node in a BST

# Key Note:
# 1. There are five situations:
# Cant find the node needed to be delete
# It's a Leaf Node(doesnt have left and right child)
# Has right child but no left child
# Has left child but no right child
# Has Both left and right child(Most complicated)
# 2. For situation 5, we can put left subtree into right subtree
# or put right subtree into left subtree, both way could work
# Let's say we are going to put left subtree into right one.
# Since we want to delete their parent node, and the slightly
# bigger node to parent node is the leftmost node of right subtree
# so we can put left subtree under leftmost node of right subtree
# 3. ## notice that we are going to append root.left under curr.left, so
# curr.left = root.left
# not
# root.left = curr.left
# 4. 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None: ### 1
            return root
        if root.val == key: 
            if root.left == None and root.right == None: ### 2
                return None
            elif root.left and root.right == None: ### 4
                return root.left
            elif root.right and root.left == None: ### 3
                return root.right
            else: ### 5
                curr = root.right
                while curr.left:
                    curr = curr.left
                curr.left = root.left ##
            return root.right
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        return root