class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.is_exist(board, i, j, word, 0):
                    return True
        return False
        
    def is_exist(self, board, x, y, word, i):
        if i == len(word):
            return True
        if  x < 0 or y < 0 or x == len(board) or y == len(board[x]):
            return False
        if board[x][y] != word[i]:
            return False
        board[x][y] = (256) ^ ord(board[x][y])
        exist = self.is_exist(board, x - 1, y, word, i + 1) \
        or self.is_exist(board, x, y - 1, word, i + 1) \
        or self.is_exist(board, x + 1, y, word, i + 1) \
        or self.is_exist(board, x, y + 1, word, i + 1)
        board[x][y] = chr((256) ^ (board[x][y]))
        return exist