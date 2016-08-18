class Solution(object):
    def twoSum(self, nums, target):
        left, right = 0, len(nums)-1
        
        while True:
            
            
            if nums[left] + nums[right] == target:
                return [left + 1, right + 1]
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1