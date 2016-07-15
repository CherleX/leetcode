class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[1:] = [nums[i] for i in range(1,len(nums)) if nums[i]!=nums[i-1]]
        return len(nums)