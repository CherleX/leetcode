class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount<0:
            return -1
        coins=sorted(coins)
        d=[amount+1]*(amount+1)
        d[0]=0
        for i in xrange(amount+1):
            for j in coins:
                if j<=i:
                    d[i]=min(d[i],d[i-j]+1)
                else:
                    break
        return -1 if d[-1]>amount else d[-1]