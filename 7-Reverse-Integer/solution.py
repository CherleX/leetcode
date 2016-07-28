class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = int(str(x)[::-1]) if x >= 0 else -int(str(x)[:0:-1])
        return 0 if res < -2147483647 or res > 2147483647 else res 