# Definition for singly-linked list.
import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 空队列
        if not lists:
            return None
        
        # 使用优先队列存储k个链表的头节点，自动取出最小的
        pq = []

        # 虚拟头节点存储新的链表
        dummy = ListNode(-1)
        p = dummy

        # pq加入元素
        for i, head in enumerate(lists):
            if head is not None:
                heapq.heappush(pq, (head.val, i, head))

        # 每次取出元素
        while pq:
            val, i, node = heapq.heappop(pq)
            p.next = node
            if node.next is not None:
                # 新添加链表后面的元素到队列
                heapq.heappush(pq, (node.next.val, i, node.next))
            p = p.next
        
        return dummy.next

        