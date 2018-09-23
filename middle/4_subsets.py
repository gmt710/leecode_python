class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 数组中只有一个数字时，返回空集合和数字本身，再新加一个数字时，
        # 将原先的所有子集加上新的数字，就是  包含新数字的子集，保留之前
        # 不包含新数字的子集。这两个子集直接相加就是新的所有子集。一样地
        # 当数组长度不断增加，我们不断往原来子集上迭代新的集合即可。
        
        # 用于保存返回值，不断插入子集
        res = [[]]
        for i in range(len(nums)):
            # 原先的所有子集加上新的数字
            for j in range(len(res)):
                res.append(res[j] + [nums[i]])
        return res
