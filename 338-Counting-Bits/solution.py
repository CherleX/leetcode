class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = []
        for i in range(num+1):
            count = 0
            while i:
                i = i&(i-1)
                count += 1
            result.append(count)
            
        return result