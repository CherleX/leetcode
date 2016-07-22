# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low ,hight,mid= 1,n,(1+n)>>1
        result = guess(mid)
        while result != 0:
            if result == -1:
                low,hight,mid = low,mid,(low+mid-1)>>1
            else:
                low,hight,mid = mid,hight,(mid+hight+1)>>1
            result = guess((mid))
            
        return mid