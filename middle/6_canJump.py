class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_step = 0
        for i in range(len(nums)-1):
            # 将max_step 更新为最大可跳跃步数
            max_step = max(max_step, (i + nums[i])) 
            # 如果最大步数止于原处
            if max_step == i:
                return False
        return True
    
