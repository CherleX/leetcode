class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count_m = count_n = 0
        m = 0
        n = 1
        
        for i in nums:
            if i == m:
                count_m += 1
            elif i == n:
                count_n += 1
            elif count_m == 0:
                count_m += 1
                m = i
            elif count_n == 0:
                count_n += 1
                n = i
            else:
                count_m -= 1
                count_n -= 1
        
        count_m = count_n = 0
        for i in nums:
            if i == m:
                count_m += 1
            if i == n:
                count_n += 1
        res = []
        if count_m > int(len(nums) / 3):
            res.append(m)
        if count_n > int(len(nums) / 3):
            res.append(n)
            
        return res
        
        
