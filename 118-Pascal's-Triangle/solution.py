class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        n, b, res = 0, [1], []
        while n < numRows:
            res.append(b)
            b = [1] + [b[i] + b[i + 1] for i in range(len(b) - 1)] + [1]
            n += 1
            
        return res