class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        import collections
        if len(nums) == 0:
            nums = []
        else: 
            # 迭代计算出0、1 和 2 元素的个数
            aa = collections.Counter(nums)
            nums1 = []
            
            for k,v in aa.items():
                for i in range(v):
                    nums1.append(k)
            # 重写当前数组
            nums[:] = nums1[:]
            
