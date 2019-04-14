class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        dp = [1] * len(nums)
        for i in range(len(nums)-1):
            for j in range(0,i+1):
                if nums[i+1] > nums[j]:
                    dp[i+1] = max(dp[i+1], dp[j]+1)
        
        return max(dp[:])
        
# nums1 = input()
# print(Solution().lengthOfLIS(nums1))
