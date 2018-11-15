class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 参考：https://blog.csdn.net/yurenguowang/article/details/77869313
        # 思想：用一个字典存储每次找到的最大连续次数中间值。遍历数组，对于数字i，
        # 找到i-1和i+1对应的value值,如果不存在则记0。
        # 然后把i的value值设为i-1,i+1的value值之和，并加1，相当于连接起来。
        # 同时置最左端和最右端的数的value值为i的value值（中间的数都已经出现过，不会再用到了）。
        # 然后更新一次最大值。

        if nums is None or len(nums) == 0:
            return 0
        m = {}
        res = 0
        for i in nums:
            if i not in m:
                # print(m)
                l = 0
                r = 0
                if i - 1 in m:
                    l = m[i - 1]
                if i + 1 in m:
                    r = m[i + 1]
                # 最大连续次数更新给其左右
                m[i] = 1 + r + l
                m[i + r] = 1 + r + l
                m[i - l] = 1 + r + l
                res = max(res, m[i])
        return res

        
        
