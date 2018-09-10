# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 0
        high = n
        
        while True:
            mid = (high+low)//2 
            if (isBadVersion(mid)) == True and isBadVersion(mid+1) == True:
                high = mid
            elif (isBadVersion(mid)) == False and isBadVersion(mid+1) == False:
                low = mid
            if (isBadVersion(mid)) == False and isBadVersion(mid+1) == True:
                return mid+1


                
