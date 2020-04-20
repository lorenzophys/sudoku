class SudokuSolver:
    def __init__(self, board):
        self.board = board

    
    def solve(self):
        if not self.empty_tile(self.board):
            return True

        row, col = self.empty_tile(self.board)

        for guess in range(1,10):
            if self.good_guess(self.board, (row,col), guess):
                self.board[row][col] = guess

                if self.solve():
                    return True

                self.board[row][col] = 0

        return False

    
    def empty_tile(self, board):
        for i in range(9):
            for j in range(9):
                if not board[i][j]:
                    return (i, j)
        return False


    def good_guess(self, board, coord, guess):
        row, col = coord
        box_x = col//3
        box_y = row//3

        for i in range(9):
            if (board[row][i] == guess):
                return False

        for i in range(9):
            if (board[i][col] == guess):
                return False

        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x*3, box_x*3 + 3):
                if (board[i][j] == guess):
                    return False

        return True


