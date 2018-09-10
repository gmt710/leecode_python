class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1,len(nums)):
            #当前值的大小与前面的值之和比较，若当前值更大，则取当前值，舍弃前面的值之和
            maxSubsum = max(nums[i]+nums[i-1], nums[i])
            #将当前和最大的赋给nums[i]，新的nums存储的为和值
            nums[i] = maxSubsum
            
        return max(nums)
    
        
