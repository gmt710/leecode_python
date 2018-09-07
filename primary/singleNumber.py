class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_times=collections.Counter(nums)
        for k,v in nums_times.items():
            if v == 1:
                return k

            
