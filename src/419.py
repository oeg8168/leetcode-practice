class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if len(board) == 0:
            return 0

        ship = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    if j > 0 and board[i][j - 1] != '.':
                        pass
                    elif i > 0 and board[i - 1][j] != '.':
                        pass
                    else:
                        ship += 1
        return ship
