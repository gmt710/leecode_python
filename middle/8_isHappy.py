class Solution(object):
    # 计算每位的平方和，返回求得的和
    def sumofsquares(self, n):
        sum_n = 0
        str_n = str(n)
        for i in range(len(str(n))):
            sum_n += pow(int(str_n[i]), 2)
            print(sum_n,str_n[i])
        return sum_n
    
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        record = []
        sum_n1 = n
        sum_n = 0
        while(sum_n != 1):
            sum_n = self.sumofsquares(sum_n1)
            if sum_n in record:
                return False
            record.append(sum_n)
            sum_n1 = sum_n
        return True
