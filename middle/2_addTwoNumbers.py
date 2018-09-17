# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        tmp = ListNode(0)
        res = tmp
        flag = 0 # 进位
        while l1 or l2:
            tmp_sum = 0
            # 如果 l1不为空，就将l1的值赋给tmp_sum
            if l1:
                tmp_sum = l1.val
                l1 = l1.next
            # 如果l1, l2不为空，就将l1+l2的值赋给tmp_sum,
            # 如何l1为空，则将l2赋值给tmp_sum
            if l2:
                tmp_sum += l2.val
                l2 = l2.next
            # tmp_sum_g求和的个位数
            tmp_sum_g = (tmp_sum + flag) % 10
            # 进位
            flag = (tmp_sum + flag) // 10
            res.next = ListNode(tmp_sum_g)
            res = res.next
        
        # 如果最后的进位不为0，则将其赋值给最高位 
        if flag:
            res.next = ListNode(1)
        
        res = tmp.next
        del tmp
        return res
            
