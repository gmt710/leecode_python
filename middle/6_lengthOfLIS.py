class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        dp = [1]*len(nums)
        for i in range(len(nums)-1):
            # 计算前i项的最长字符串个数，并与i+1项进行比较，
            # 得到i+1项的最长字符串个数
            for j in range(0,i+1):
                if nums[i+1] > nums[j]:
                    dp[i+1] = max(dp[i+1],dp[j]+1)
        return max(dp)
    
