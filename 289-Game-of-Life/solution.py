class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[i])):
                count = self.get_neighbour(board, i, j)
                if board[i][j] == 1:
                    if count == 2 or count == 3:
                        board[i][j] = 3
                else:
                    if count == 3:
                        board[i][j] = 2
        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j] = board[i][j]>>1 

    def get_neighbour(self, board, raw, col):
        count = 0
        for i in range(raw - 1, raw + 2):
            for j in range(col - 1, col + 2):
                if 0 <= i and i < len(board) and 0 <= j and j < len(board[0]):
                    count += board[i][j] & 1
                    
        count -= board[raw][col]
        return count
                    