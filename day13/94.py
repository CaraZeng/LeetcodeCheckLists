# inorder
# Key Note:
# 1. iterate to the base left node, then mid, then right.
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        if not root:
            return []
        stack = []  # 不能提前将root节点加入stack中

        result = []
        cur = root
        while cur or stack:
            # 先迭代访问最底层的左子树节点
            if cur:     
                stack.append(cur)
                cur = cur.left		
            # 到达最左节点后处理栈顶节点    
            else:		
                cur = stack.pop()
                result.append(cur.val)
                # 取栈顶元素右节点
                cur = cur.right	
        return result