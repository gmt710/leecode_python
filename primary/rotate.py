class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        numi = len(nums)
        nums[:] = nums[numi-k:] + nums[:numi-k]

        
