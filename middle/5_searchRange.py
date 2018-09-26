class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 设置左右两个指针进行二分法，当通过二分法搜寻到目标值时，
        # 左右指针合一，然后在合一的位置上分别向左向右遍历寻找是否
        # 还有和目标值相等的数。
        List = [-1,-1]
        # 如果nums为空，则返回[-1,-1]
        if len(nums) == 0:
            return List
        # 如果比最小值小或者比最大值大，即不在nums内，则返回[-1,-1]
        elif target < nums[0] or target > nums[-1]:
            return List
        else:
            left = 0
            right = (len(nums)-1)
            # 使用二分法查找
            while(left <= right):
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                # 找到target以后，left，right分别向左向右找到初始与结束位置
                elif nums[mid] == target:
                    left = right = mid
                    while left-1 >= 0 and nums[left-1] == target:                        
                        left -= 1                    
                    while right+1 <= len(nums)-1 and nums[right+1] == target:
                        right += 1   
                    List = [left, right]
                    return List
        return List

                
            
        
        
