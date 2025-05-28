# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def trainingPlan(self, head: Optional[ListNode], cnt: int) -> Optional[ListNode]:
        """ 
        双指针:p1从head先走k步,p2和p1再同时走,当p1为null时p2就是倒数第k个节点
        """

        p1, p2 = head, head
        for i in range(cnt):
            p1 = p1.next

        while p1 is not None:
            p2 = p2.next
            p1 = p1.next

        return p2