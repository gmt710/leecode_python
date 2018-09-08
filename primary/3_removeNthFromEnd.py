# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        List = []
        count = 0
        while(head):
            List.append(head)
            head = head.next
            count += 1
        
        if count == 1:
            return None
        if n == 1:
            List[-2].next = None
            return List[0]
        else:
            List[-n].val = List[-n].next.val
            List[-n].next = List[-n].next.next
            return List[0]
        
            
        
