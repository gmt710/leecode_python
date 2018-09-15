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
                while(left < right):
                    sum_nums = nums[i] + nums[left] + nums[right]
                    if sum_nums == 0:
                        list_nums.append([nums[i],nums[left],nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                    if sum_nums < 0:
                        left += 1
                    if sum_nums > 0:
                        right -= 1
        return list_nums

                
                
        
