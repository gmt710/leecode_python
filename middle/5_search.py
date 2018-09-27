class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 如果target在nums中，返回target在nums中的索引
        if target in nums:
            res = nums.index(target)
        # 不在，返回-1
        else:
            res = -1
        return res
