class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # http://bookshadow.com/weblog/2015/09/28/leetcode-find-duplicate-number/
        # 由于重复数字的存在，那么一定会形成环，我们用快慢指针可以找到环并确定环的起始位置

        slow = 0
        fast = 0
        t = 0
        # 
        while True: 
            slow = nums[slow]
            fast = nums[nums[fast]]
            if (slow == fast):
                break
            
            
        while True:
            slow = nums[slow]
            t = nums[t]
            
            if (slow == t): 
                break
      
        return slow
