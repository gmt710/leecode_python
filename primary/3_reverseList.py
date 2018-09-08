# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head == None:
            return []
        
        temp_last = None
        temp_head = head
        while(temp_head):
            temp_next = temp_head.next
            temp_head.next = temp_last
            temp_last = temp_head
            temp_head = temp_next
        return temp_last
        
