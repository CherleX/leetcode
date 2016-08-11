class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in xrange(0,32):
            count = 0
            for a in nums:
                if ((a >> i) & 1):
                    count+=1
            ans |= ((count%3) << i)
        return self.convert(ans)
        
    def convert(self,x):
        if x >= 2**31:
            x -= 2**32
        return x