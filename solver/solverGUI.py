from settings import *
import pygame, sys, time


class SudokuSolver:
    def __init__(self, board):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Sudoku")
        self.font = pygame.font.SysFont("arial", int(TILE*0.7))
        self.is_running = True
        self.board = board
        self.draw(self.window)
        print("Press SPACE to solve!")

    
    def solve(self):
        if not self.empty_tile(self.board):
            return True

        row, col = self.empty_tile(self.board)

        for guess in range(1,10):
            if self.good_guess(self.board, (row, col), guess):
                self.board[row][col] = guess
                self.draw(self.window)
                pygame.display.update()
                self.clock.tick(FPS)

                if self.solve():
                    return True

                self.board[row][col] = 0
                self.draw(self.window)
                pygame.display.update()
                self.clock.tick(FPS)

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

    #GUI stuff

    def draw(self, window):
        self.window.fill(WHITE)
        self.draw_numbers(window)

        pygame.draw.rect(window, BLACK, (OFFSET, OFFSET, WIDTH-2*OFFSET, HEIGHT-2*OFFSET), 3)
        for i in range(1,9):
            if i % 3 != 0:
                pygame.draw.line(window, BLACK, (OFFSET+i*TILE, OFFSET), (OFFSET+i*TILE, WIDTH-OFFSET), 1)
                pygame.draw.line(window, BLACK, (OFFSET, OFFSET+i*TILE), (HEIGHT-OFFSET, OFFSET+i*TILE), 1)
            else:
                pygame.draw.line(window, BLACK, (OFFSET+i*TILE, OFFSET), (OFFSET+i*TILE, WIDTH-OFFSET), 3)
                pygame.draw.line(window, BLACK, (OFFSET, OFFSET+i*TILE), (HEIGHT-OFFSET, OFFSET+i*TILE), 3)


    def draw_numbers(self, window):
        for i in range(9):
            for j in range(9):
                if self.board[i][j]:
                    font = self.font.render(str(self.board[i][j]), True, BLACK)
                    #this is needed to put the number in the center
                    font_width = font.get_width()
                    font_height = font.get_height()
                    coordinates = (i*TILE+OFFSET+(TILE-font_width)//2,j*TILE+OFFSET+(TILE-font_height)//2)
                    window.blit(font, coordinates)


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.solve()


    def main(self):
        while self.is_running:
            self.check_events()
            self.clock.tick(FPS)
            pygame.display.update()

        pygame.quit()
        sys.exit()
