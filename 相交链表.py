# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """  
        双指针:p1指针从A走，p2指针从B走，当p1指针为null时，转到headB
        当p2指针为null时，转到headA。当p1 = p2时，就是相交的节点
        """

        if not headA or not headB:
            return None
        
        p1, p2 = headA, headB
        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1