class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 超时
        # for i in range(len(nums)+1):
        #     if i not in nums:
        #         return i
        
        # 换一种思路
        n = len(nums)
        All_sum = int(n*(n+1)/2)
        Part_sum = sum(nums)
        loss_num = All_sum - Part_sum
        return loss_num
