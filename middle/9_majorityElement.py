class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import collections
        # 计数
        counter = collections.Counter(nums)
        # k是值，v是值的个数
        for k,v in counter.items():
            if v > len(nums)/2:
                return k
            
