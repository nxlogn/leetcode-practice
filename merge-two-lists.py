from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 每次添加两个链表中相对较小的元素到新的链表中
        # 最后将剩下的元素加入到末尾
        # 返回新链表
        p1, p2 = list1, list2
        head = ListNode()
        p = head
        while p1 != None and p2 != None:
            if p1.val < p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next
        if p1 != None:
            p.next = p1
        if p2 != None:
            p.next = p2
        return head.next