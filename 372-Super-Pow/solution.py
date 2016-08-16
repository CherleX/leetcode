class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        mod1 = mod = a % 1337
        period = 0
        while True: 
            mod = mod * mod1 % 1337
            period += 1
            if mod == mod1:
                break
        b = int(''.join(str(i) for i in b))
        b_adjusted = b % period
        return (mod ** b_adjusted) % 1337