# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):     
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        # intervals按start大小排序
        intervals.sort(key=lambda x: x.start)
        merged = []
        for interval in intervals:
            # 如果区间尾小于区间头，说明没有交集，不需要合并，直接放入merged中
            if not merged or merged[-1].end < interval.start:
                merged.append(interval)
            # 有交集，比较哪个区间尾大，进行合并
            else:
                merged[-1].end = max (merged[-1].end, interval.end)
                
        return merged
