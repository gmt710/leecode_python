class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        list_nums = []
        nums.sort()
        i = 0
        for i in range(len(nums)-2):
            if i == 0 or nums[i] > nums[i-1]:
                left = i+1
                right = len(nums)-1
                
                #截止条件,直到left=right
                while(left < right):
                    sum_nums = nums[i] + nums[left] + nums[right]
                    if sum_nums == 0:
                        list_nums.append([nums[i],nums[left],nums[right]])
                        left += 1
                        right -= 1
                        # 如果left存在重复,则向右遍历
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        # 如果right存在重复,则向左遍历
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                    # 如果和小于零说明left小了,left向右遍历
                    if sum_nums < 0:
                        left += 1
                    # 如果和大于零说明right大了,right向左遍历
                    if sum_nums > 0:
                        right -= 1
        return list_nums

                
                
        
