class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        num_0 = 0
        nums1 = []
        print(len(nums))
        for i in range(len(nums)):
            if nums[i] == 0:
                num_0 += 1
            else:
                nums1.append(nums[i])
            print(i)
        for j in range(num_0):
            nums1.append(0)
        nums[:] = nums1[:]
# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         count_num = collections.Counter(nums)
#         for i in range(int(count_num[0])):
#             nums.remove(0)
#             nums.append(0)
        
        
