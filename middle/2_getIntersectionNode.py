# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1 = headA
        p2 = headB
        while(p1 != p2):
            # p1 = headB,p2 = headA使得两个比较的链表长度相同，在第一个交点处相同
            # p1 a1->a2->c1->c2->c3-> b1->b2->b3->[c1]->c2->c3->None
            # p2 b1->b2->b3->c1->c2->c3-> a1->a2->[c1]->c2->c3->None
            if p1 == None:
                p1 = headB
            else:
                p1 = p1.next
            if p2 == None:
                p2 = headA
            else:
                p2 = p2.next
            # p1 = headB if p1 == None else p1.next
            # p2 = headA if p2 == None else p2.next

        return p1
        
