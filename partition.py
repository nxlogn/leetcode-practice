# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # 将链表中小于x的元素复制到链表A中
        # 将链表中大于x的元素复制到链表B中
        # 将A和B合并
        listA = ListNode(-1)
        listB = ListNode(-1)
        pA = listA
        pB = listB

        pHead = head
        while pHead != None:
            if pHead.val < x:
                pA.next = pHead
                pA = pA.next
            else:
                pB.next = pHead
                pB = pB.next
            # 断掉原链表的链接
            temp = pHead.next
            pHead.next = None
            pHead = temp
        
        pA.next = listB.next
        return listA.next
