class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[1],nums[0])
        for i in range(2,len(nums)):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])
            
        return dp[len(nums)-1]
    
#         last = 0 
#         now = 0
#         for i in nums: 
#             #python可以同时给多个变量赋值
#             #last = now 这个赋的值now为上一次的now，
#             #now = max(last + i, now)这里作比较的值last是上一次的last
#             [last, now] = (now, max(last + i, now))
            
#         return now
