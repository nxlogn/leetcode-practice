# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self) -> None:
        # 最大直径
        self.res = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.maxDepth(root)
        return self.res

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        # 递归左右子树
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        
        # 更新最大直径（左子树深度 + 右子树深度）
        self.res = max(leftDepth + rightDepth, self.res)
        
        # 返回当前节点的最大深度
        return max(leftDepth, rightDepth) + 1