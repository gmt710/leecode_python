class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 找连续的递增的三元子序列
#         if len(nums) < 3:
#             return False
        
#         for i in range(2,len(nums)):
#             j = 0
#             while j <= (len(nums)-3):
#                 str_nums = nums[j:j+3]
#                 print(str_nums)
#                 if  str_nums[0] < str_nums[1] and str_nums[1] < str_nums[2]:
#                     return True
#                 j += 1
#         return False

        # 递增的三元子序列
        res = [float('inf'),float('inf')]
        for n in nums:
            if n > res[1]:
                return True
            if n <= res[0]:
                res[0] = n
            else:
                res[1] = n
        return False
    
