# Definition for a binary tree node.
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:

    def __init__(self) -> None:
        self.res = []

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.traverse(root)
        return self.res

    def traverse(self, root:TreeNode) -> None:
        # 空节点
        if not root:
            return
        
        # 当前节点操作
        self.res.append(root.val)
        # 递归左右子节点
        self.traverse(root.left)
        self.traverse(root.right)
        