class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 我想的是用数组，参考的别人的用的哈希，好像是很快。
        # 参考网址：https://blog.csdn.net/xiaoxiaoley/article/details/78643496
        # 要求O（n）的复杂度，可以用哈希表来存储1到n的内容。
        # 先遍历一遍原数组，将原数组中的1-n的整数存入哈希表对应0到n-1的位置。
        # 再对哈希表进行遍历，遍历到存储内容为空的，则返回遍历到整数的索引值，即为第一个丢失的正整数。
        
        if len(nums) == 0:
            return 1
        
        hashed_nums = [0]*len(nums)
        for i in range(len(nums)):
            # 如果大于0，并且小于len(nums),就将其索引对应的位+1，进行标记
            # 只需要比较nums[i] <= n,而不是更大的数，
            # 是因为总共n个数，如果有大于n的数，说明n之前一定有丢失的数
            if nums[i] > 0 and nums[i] <= len(nums):
                hashed_nums[nums[i]-1] += 1
        
        for i in range(len(nums)):
            if hashed_nums[i] == 0:
                return i+1
        # 如果遍历到末尾还没有丢失的话，说明末尾的后一个为最小的丢失正数
        return len(nums)+1
    
    
    
