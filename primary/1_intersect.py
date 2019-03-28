class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if nums1 == None or nums2 == None:
            return []
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        nums = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] == nums2[j]:
                nums.append(nums1[i])
                i += 1
                j += 1
        return nums
        
        
class Solution:
#     def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         nums = []
#         len_nums1 = len(nums1)
#         len_nums2 = len(nums2)
#         lens = min(len_nums1, len_nums2)
#         count_nums1 = collections.Counter(nums1)
#         count_nums2 = collections.Counter(nums2)
#         for i in range(lens):
#             if len_nums1 <= len_nums2:
#                 if nums1[i] in nums2[:] and count_nums2[nums1[i]]:
#                     nums.append(nums1[i])
#                     count_nums2[nums1[i]] -= 1
#             else:
#                 if nums2[i] in nums1[:] and count_nums1[nums2[i]]:
#                     nums.append(nums2[i])
#                     count_nums1[nums2[i]] -= 1
#                     print(nums)
#         return nums[:]
    
