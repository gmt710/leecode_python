# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # https://blog.csdn.net/qq_34364995/article/details/80994110
        # 先将链表递归由中间分成两个链表，然后在将这两个链表作比较，得到一个排序链表
        # 即不断将由中点分成的两个链表进行排序
        
        #     ********               |   ^
        #　****       ****           |   |
        #  ** **      ** **          |   |
        # * *  * *   * *  * *        V   |
        
        if head is None or head.next is None:
            return head
        mid = self.get_mid(head)
        left = head
        right = mid.next
        mid.next = None
        # 次数递归
        return self.merge(self.sortList(left), self.sortList(right))
    
    def merge(self, p, q):
        # 按小大顺序合并两个链表
        tmp = ListNode(0)
        cur = tmp
        while p and q:
            if p.val < q.val:
                cur.next = p
                p = p.next
            else:
                cur.next = q
                q = q.next

            cur = cur.next
            
        if p:
            cur.next = p
        else:
            cur.next = q
        return tmp.next
            
        
    
    def get_mid(self, head):
        # 链接中作者使用的是快慢指针，快指针走完全程时，慢指针才走了一半距离
        if head is None:
            return None
        fast = slow = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow


        
