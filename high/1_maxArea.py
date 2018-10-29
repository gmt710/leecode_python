class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # if len(height) == 2:
        #     return min(height[0],height[1])
        
        # 参考：https://blog.csdn.net/chenhua1125/article/details/80502764
        # 逼近法
        # 找两边组成最大面积的边界
        # 每次左右两端都舍去短的那一端 
        left = 0
        right = len(height)-1
        max_area = 0
        
        while left < right:
            # 将当前计算的最大面积与之前得到的最大面积进行比较
            # 当前最大面积由，找到的两边界中最小长度*两边界的宽
            max_area = max(max_area, min(height[left], height[right])*(right-left))
            
            # 如果左边界更小的话，由左边界的右边的一个边界继续计算比较；
            # 否则从右边界的左边的一个边界继续计算比较
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
        
