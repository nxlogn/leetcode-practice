# Definition for a binary tree node.
# 题号104
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    
    def __init__(self) -> None:
        self.depth = 0 # 节点深度
        self.res = 0 # 最大深度

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.res

    def traverse(self, root:TreeNode) -> None :
        if not root:
            return
        
        # 当前节点操作
        self.depth += 1
        # 到达根节点
        if not root.left and not root.right:
            self.res = max(self.res, self.depth)
        # 递归左右节点
        self.traverse(root.left)
        self.traverse(root.right)
        # 退出当前节点
        self.depth -= 1