class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 别人的思想：利用返回的列表从前往后算一遍，再从后往前算一次即可
        # 引自：http://www.bubuko.com/infodetail-1410535.html
        
        result = [1]
        #  利用返回的列表从前往后算一遍
        for i in range(1,len(nums)):
            result.append(result[i-1] * nums[i-1])

        product = 1
        # range(start, stop, step)
        # range(0, 30, 5)  # 步长为 5 [0, 5, 10, 15, 20, 25]
        # 再从后往前算一次即可
        for i in range(len(nums)-1,-1,-1):
            result[i] = product * result[i]
            # print(result)
            product *= nums[i]

        return result
    
        
