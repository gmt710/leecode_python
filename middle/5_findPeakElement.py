class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(N) 时间复杂度
        # 顺序方式：从第一个元素开始，若其大于相邻的后续元素，
        # 则第一个元素就是一个局部最大值，返回即可。若其小于
        # 相邻的后续元素，则第二个元素大于第一个元素。如此，
        # 一一遍历数组，第一次出现，第i个元素若大于其相邻后续
        # 元素，则该元素就是一个局部最大值
        
        # if len(nums) == 0 or len(nums) == 1:
        #     return 0
        # for i in range(1,len(nums)):
        #     if nums[i-1] > nums[i]:
        #         return i-1
        # return len(nums)-1
        
        # 二分查找：如果中间元素大于其相邻后续元素，则中间元素
        # 左侧(包含该中间元素）必包含一个局部最大值。如果中间
        # 元素小于其相邻后续元素，则中间元素右侧必包含一个局部最大值。
        
        left = 0
        right = len(nums) - 1
        while left <= right:
            if left == right:
                return left
            mid = left + (right -left) / 2 
            # 如果中间小于右边，那么一定在右边
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                # right不可以是mid-1，万一正好是mid，就跳过了，因为并没有比对mid的值
                right = mid
                
