class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # 先统计数组中各个任务出现的次数。优先安排次数最多的任务。
        # 次数最多的任务安排完成之后所需的时间间隔为（max(次数)-1）*（n+1）+1。
        # 其余任务直接插空即可。
        import collections
        counter = collections.Counter(tasks)
        
        count = 0
        len_o = 0
        max_o = max(counter.values())
        for i in counter.values():
            if i==max_o:
                count = count+1
                print(count)   
        return max(len(tasks),(max_o-1)*(n+1)+count)
