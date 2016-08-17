class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count_m = 0
        m = 0
        
        for i in nums:
            if i == m:
                count_m += 1
            elif count_m == 0:
                count_m += 1
                m = i
            else:
                count_m -= 1
        return m
        
        
