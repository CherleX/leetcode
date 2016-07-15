from functools import reduce


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = set()
        while n != 1:
            if n in visited:
                return False
            visited.add(n)
            n = reduce(lambda x, y: x + y, map(lambda x: int(x) ** 2, list(str(n))))
        return True
