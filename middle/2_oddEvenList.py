# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None or head.next.next == None:
            return head
        
        p = head.next # 偶数位
        q = head.next.next #奇数位
        head.next = q
        t = p #保存p偶数位的头指针
        while(q.next):
            p.next = p.next.next
            p = p.next
            q.next = q.next.next
            if (q.next):
                q = q.next
        q.next = t #链接偶数位
        p.next = None #尾指针
        return head 
        
        
        
