# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """ 
        找到倒数第k+1个节点,改变next指针
        """
        # 避免head节点被删除，使用dummy虚拟头节点
        dummy = ListNode(-1)
        dummy.next = head

        x = self.findFromEnd(dummy, n + 1)
        x.next = x.next.next
        return dummy.next

    def findFromEnd(self, head:ListNode, k:int):
        """  
        双指针实现
        """
        p1, p2 = head, head
        for _ in range(k):
            p1 = p1.next
        while p1:
            p2 = p2.next
            p1 = p1.next
        return p2