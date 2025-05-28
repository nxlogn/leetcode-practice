# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ 
        p1指针每次走两步,p2指针每次走1步
            1.如果是奇数长度的链表,则当p1.next是none的时候p2指针就是中间节点
            2.如果是偶数长度的链表,则当p1是none的时候p2指针就是中间节点
        """

        p1, p2 = head, head
        if not head:
            return None
        
        while p1 and p1.next:
            p1 = p1.next.next
            p2 = p2.next
        return p2