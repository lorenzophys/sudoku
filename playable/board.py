import pygame
from settings import *


class Board:
    def __init__(self):
        self.font = pygame.font.SysFont("arial", int(TILE*0.7))
        self.grid = BOARD
        self.tile_selected = None
        self.fixed_numbers = []
        self.find_fixed_numbers(self.grid)
        self.is_complete = False
        self.solution_correct = False


    def draw(self, window):
        self.highlight_selected_tile(window, self.tile_selected)
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
                if self.grid[i][j]:
                    font = self.font.render(str(self.grid[i][j]), True, BLACK)
                    #this is needed to put the number in the center
                    font_width = font.get_width()
                    font_height = font.get_height()
                    coordinates = (i*TILE+OFFSET+(TILE-font_width)//2,j*TILE+OFFSET+(TILE-font_height)//2)
                    window.blit(font, coordinates)


    def highlight_selected_tile(self, window, selected):
        if self.tile_selected and self.tile_selected not in self.fixed_numbers:
            pygame.draw.rect(window, PINK, (selected[0]*TILE+OFFSET+1, selected[1]*TILE+OFFSET+1, TILE, TILE))


    def find_fixed_numbers(self, grid):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j]:
                    self.fixed_numbers.append((i,j))


    def is_board_complete(self):
        check_set = set()
        for i in range(9):
            for j in range(9):
                check_set.add(self.grid[i][j])
        if not(0 in check_set):
            self.is_complete = True
        else:
            self.is_complete = False


    def check_row(self):
        check = list()
        for i in range(9):
            row_set = set()
            for j in range(9):
                row_set.add(self.grid[j][i])
            if len(row_set) == 9:
                check.append(True)
            else:
                check.append(False)
        if False in check:
            return False
        else:
            return True
                
    
    def check_col(self):
        check = list()
        for j in range(9):   
            col_set = set()
            for i in range(9):
                col_set.add(self.grid[j][i])
            if len(col_set) == 9:
                check.append(True)
            else:
                check.append(False)
        if False in check:
            return False
        else:
            return True


    def check_box(self):
        check = list()
        for x in range(3):
            for y in range(3):
                box_set = set()
                for x1 in range(3):
                    for y1 in range(3):
                        i = x*3 + x1
                        j = y*3 + y1
                        box_set.add(self.grid[j][i])
                if len(box_set) == 9:
                    check.append(True)
                else:
                    check.append(False)
        if False in check:
            return False
        else:
            return True

    
    def check_solution(self):
        if self.is_complete:
            self.solution_correct = self.check_row() and self.check_col() and self.check_box()

