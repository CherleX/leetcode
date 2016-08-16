class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n == 1:
            return 10
        n = min(n, 10)
        res = 10
        for i in range(1, n):
            g = 9
            for j in range(1, i + 1):
                g *= (10 - j)
            res += g
            
        return res