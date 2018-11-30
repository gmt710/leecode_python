class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums_len = len(nums)
        length = nums_len-k+1
        num = []
        if nums == []:
            return []
        for i in range(length):
            num.append(max(nums[i:i+k]))
        
        return num
    
    
