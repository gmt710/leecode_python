# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# heapq使用说明
# a为普通列表 
# - heapq.heapify(a) 调整a，使得其满足最小堆 
# - heapq.heappop(a) 从最小堆中弹出最小的元素 
# - heapq.heappush(a,b) 向最小堆中压入新的元素

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # https://blog.csdn.net/iyuanshuo/article/details/79600011
        # 思想：首先将每个list里面的第一个元素，也就是每个list的最小元素（因为list都是已排序），
        # 共K个指放入大小为K的堆中，将其维护成最小堆结构。每次将堆顶的元素，也就是最小元素放到结果中，
        # 然后取出该元素原先所处的list中的下一个元素放入队中，维护最小堆结构。
        # 当所有元素读取完，所有的元素就按照从小到大放到结果链表中。
        
        import heapq
        # 用于保存最小堆
        heap = []
        for ln in lists:
            if ln:
                # 将k 个排序链表的第一个元素及其指针放进去，即最小的元素
                heap.append((ln.val, ln))
        dummy = ListNode(0)
        cur = dummy
        # 调整heap，使其满足最小堆
        heapq.heapify(heap)
        while heap:
            # 将最小堆中最小的元素值及其指针返回
            valu, ln_index = heapq.heappop(heap)
            cur.next = ln_index
            cur = cur.next
            # 如果刚放入结果中的元素指针后还有元素的情况下，将其后的元素及指针放进去
            if ln_index.next:
                heapq.heappush(heap, (ln_index.next.val, ln_index.next))
        return dummy.next
