class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        # 引自：https://blog.csdn.net/ma412410029/article/details/80800930
        from collections import defaultdict
        # defaultdict的作用是在于，当字典里的key不存在但被查找时，返回的不是keyError而是一个默认值,
        # defaultdict(int):返回0
        d1 = defaultdict(int)
        # A和B中所有的两数之和对应的个数
        for item1 in A:
            for item2 in B:
                d1[item1+item2] += 1
 
        d2 = defaultdict(int)
        # C和D中所有的两数之和对应的个数
        for item1 in C:
            for item2 in D:
                d2[item1+item2] += 1
        
        count = 0
        # 计数，如果A和B中所有的两数之和，等于负的C和D中所有的两数之和
        # 说明A、B、C、D四个数相加等于0
        # d1[item] * d2[-item]:是因为，取值为item的两数和有d1[item]种，
        # 取值为-item的两数和有d2[-item]种，最终得0的有d1[item] * d2[-item]种
        for item in d1.keys():
            if -item in d2:
                count += d1[item] * d2[-item]
        return count

    
