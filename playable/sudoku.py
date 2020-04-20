import sys, pygame
from settings import *
from board import Board


class Sudoku:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Sudoku")
        self.is_running = True
        self.mouse_position = None
        self.board = Board()


    def draw_board(self):
        self.window.fill(WHITE)
        self.board.draw(self.window)


    def get_tile_clicked(self):
        def mouse_inside_board():
            if self.mouse_position[0] < OFFSET or self.mouse_position[1] < OFFSET:
                return False
            elif self.mouse_position[0] > TILE*9 or self.mouse_position[1] > TILE*9:
                return False
            else:
                return True

        if mouse_inside_board():
            x_tile = int((self.mouse_position[0]-OFFSET)//TILE)
            y_tile = int((self.mouse_position[1]-OFFSET)//TILE)
            return (x_tile, y_tile)
        else:
            return None


    def update(self):
        self.mouse_position = pygame.mouse.get_pos()
        self.get_tile_clicked()
        pygame.display.update()


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.board.tile_selected = self.get_tile_clicked()
            if event.type == pygame.KEYDOWN:
                if self.board.tile_selected != None and self.board.tile_selected not in self.board.fixed_numbers:
                    #check if you press a number or a letter
                    try:
                        self.board.grid[self.board.tile_selected[0]][self.board.tile_selected[1]] = int(event.unicode)
                        self.board.is_board_complete()
                        if self.board.is_complete:
                            print("Board complete")
                            self.board.check_solution()
                            if self.board.solution_correct:
                                print("WIN")
                    except:
                        continue
                

    def main(self):
        while self.is_running:
            self.check_events()
            self.draw_board()
            self.update()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()
