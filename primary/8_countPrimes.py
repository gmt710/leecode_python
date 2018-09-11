class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 算法超时
#         if n < 3:
#             return 0
    
#         r = []
#         r.append(2)
#         #从3开始挨个筛选
#         for a in range(3,n):
#             b=False

#             #用a除以小于a的质数b
#             for b in r:
#                 if a%b==0:
#                     b=False
#                     break
#                 else:
#                     b=True
#             if b==True:
#                 r.append(a)
#         return len(r)

        # 厄拉多塞筛法
        # 厄拉多塞筛法(Sieve of Eeatosthese)。
        #具体操作：先将 2~n 的各个数放入表中，然后在2的上面画一个圆圈，然后划去2的其他倍数；第一个既未画圈又没有被划去的数是3，将它画圈，再划去3的其他倍数；现在既未画圈又没有被划去的第一个数 是5，将它画圈，并划去5的其他倍数……依次类推，一直到所有小于或等于 n 的各数都画了圈或划去为止。这时，表中画了圈的以及未划去的那些数正好就是小于 n 的素数。
        
        if n < 3:
            return 0
        primes = [1] * n
        primes[0] = primes[1] = 0
        
        for i in range(int(n/2)+1):
            if primes[i] == 1:
                # [i*i:n:i] 列表从i*i到n,将i的倍数不是质数，置为0
                primes[i*i:n:i] = [0] * len(primes[i*i:n:i])
        return sum(primes)
        
        
        
