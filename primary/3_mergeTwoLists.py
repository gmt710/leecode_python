# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        newHead = ListNode(0)
        p = l1
        q = l2
        r = newHead
        
        while p and q:
            if p.val <= q.val:
                r.next = p
                r = p
                p = p.next
            else:
                r.next = q
                r = q
                q = q.next
        if p == None:
            p = q
        r.next = p
        return newHead.next
                
        
        
