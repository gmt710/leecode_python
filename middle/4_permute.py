class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1: 
            return [nums]
        ans = []
        for i, num in enumerate(nums):
            n = nums[:i] + nums[i+1:]
            
            # 将得到少数位组合，再基础上再进行组合
            for temp_list in self.permute(n):
                ans.append([num] + temp_list)

        return ans
