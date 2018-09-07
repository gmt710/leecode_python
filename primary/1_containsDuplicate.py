class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_times=collections.Counter(nums)
        for i in nums_times.values():
            if i > 1:
                return True
        return False
            

        
