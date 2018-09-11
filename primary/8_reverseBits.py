class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # {:b}'.format(n) 转换位二进制
        l = list('{0:032b}'.format(n))
        # 将其颠倒
        l.reverse()
        # 将字符连成字符串，int(str,2)  并将二进制字符串转换成十进制
        r = int(''.join(l),2)
        return r
        
