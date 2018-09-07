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
        
        
