class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0: return -1
        
        left = 0
        right = (len(nums))-1
        while left < right:
            mid = (left+right)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        index = left    
        print(index)
        res_index = self.binary_find(target, nums[:index])
        if res_index == -1:
            res_index = self.binary_find(target, nums[index:])
            if res_index != -1:
                res_index += index

        return res_index
    
    def binary_find(self, target, nums):
        index = -1
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if target < nums[mid]:
                r = mid -1
            elif target > nums[mid]:
                l = mid + 1
            else:
                index = mid
                break
        return index
    
                
        
