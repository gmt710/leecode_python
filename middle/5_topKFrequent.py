class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import collections
        # 计数
        aa = collections.Counter(nums)
        # 找出出现频率前 k 高的元素 与 次数
        b = aa.most_common(k)
        # most_k出现频率前 k 高的元素
        most_k = [b[i][0] for i in range(k)]
        return most_k
