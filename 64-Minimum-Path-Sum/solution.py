class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        row, col = len(grid), len(grid[0])
        
        dp = [0] * col
        
        dp[0] = grid[0][0]
        for i in range(row):
            for j in range(col):
                if i == 0 and j == 0: continue
                
                if i == 0:
                    dp[j] = dp[j-1] + grid[i][j]
                elif j == 0:
                    dp[j] = dp[j] + grid[i][j]
                else:
                    dp[j] = min(dp[j-1], dp[j]) + grid[i][j]
        
        return dp[col - 1]
