class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(numRows):
            # 需先创建一行
            res.append([1])
            #在列上添加元素
            for j in range(1,i+1):
                if j == i:
                    res[i].append(1)
                else:
                    res[i].append(res[i-1][j-1]+res[i-1][j])
        return res
                
        
