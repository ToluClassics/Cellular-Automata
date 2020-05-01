# import pygame
# start drawing
import sys, pygame
import random
import time
from datetime import datetime

import pygame.draw

BOARD_SIZE = WIDTH, HEIGHT = 640, 480
CELL_SIZE = 10
DEAD_COLOR = 0, 0, 0
ALIVE_COLOR = 0, 255, 255

MAX_FPS = 10.0



class LifeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(BOARD_SIZE)
        self.clearscreen()
        self.last_update_completed = datetime.now().microsecond
        self.active_grid = 0
        self.grids=[]
        self.num_columns = int(WIDTH / CELL_SIZE)
        self.num_rows = int(HEIGHT / CELL_SIZE)
        self.init_grid()

    def init_grid(self):

        def create_grid():
            rows = []
            for row_num in range(self.num_rows):
                list_of_columns = [0]*self.num_columns
                rows.append(list_of_columns)
            return rows

        self.grids.append(create_grid())
        self.grids.append(create_grid())

        self.set_grid()


    # set_grid(0) = all dead
    # set_grid(1) = all alive
    # set_grid() = random
    # set_grid(None) = random

    def set_grid(self,value=None):
        for row in range(self.num_rows):
            for col in range(self.num_columns):
                if value == None:
                    cell_value = random.randint(0,1)
                else:
                    cell_value = value
                self.grids[self.active_grid][row][col] = cell_value

    def clearscreen(self):
        self.screen.fill(DEAD_COLOR)

    def get_cell(self, row_num, col_num):
        """
        Get the alive/dead (0/1) state of a specific cell in active grid
        :param row_num:
        :param col_num:
        :return: 0 or 1 depending on state of cell. Defaults to 0 (dead)
        """
        try:
            cell_value = self.grids[self.active_grid][row_num][col_num]
        except:
            cell_value = 0
        return cell_value

    def check_cell_neighbors(self, row_index, col_index):
        """
        Get the number of alive neighbor cells, and determine the state of the cell
        for the next generation. Determine whether it lives, dies, survives, or is born.
        :param row_index: Row number of cell to check
        :param col_index: Column number of cell to check
        :return: The state the cell should be in next generation (0 or 1)
        """
        num_alive_neighbors = 0
        num_alive_neighbors += self.get_cell(row_index - 1, col_index - 1)
        num_alive_neighbors += self.get_cell(row_index - 1, col_index)
        num_alive_neighbors += self.get_cell(row_index - 1, col_index + 1)
        num_alive_neighbors += self.get_cell(row_index, col_index - 1)
        num_alive_neighbors += self.get_cell(row_index, col_index + 1)
        num_alive_neighbors += self.get_cell(row_index + 1, col_index - 1)
        num_alive_neighbors += self.get_cell(row_index + 1, col_index)
        num_alive_neighbors += self.get_cell(row_index + 1, col_index + 1)

        # Rules for life and death
        if self.grids[self.active_grid][row_index][col_index] == 1:  # alive
            if num_alive_neighbors > 3:  # Overpopulation
                return 0
            if num_alive_neighbors < 2:  # Underpopulation
                return 0
            if num_alive_neighbors == 2 or num_alive_neighbors == 3:
                return 1
        elif self.grids[self.active_grid][row_index][col_index] == 0:  # dead
            if num_alive_neighbors == 3:
                return 1  # come to life

        return self.grids[self.active_grid][row_index][col_index]

    def update_generation(self):
        # inspect current active generation
        # update inactive grid to store next gen
        for row in range(self.num_rows):
            for col in range(self.num_columns):
                next_gen_state = self.check_cell_neighbors(row,col)
                #set inactive grid future cell state
                self.grids[self.inactive_grid()][row][col] = next_gen_state
        # swap out the inactive grid
        self.active_grid = self.inactive_grid()

    def inactive_grid(self):
        """
        Simple helper function to get the index of the inactive grid
        If active grid is 0 will return 1 and vice-versa.
        :return:
        """
        return (self.active_grid + 1) % 2

    def draw_grid(self):
        #pygame.draw.circle(self.screen, ALIVE_COLOR, [50, 50], 5)
        self.clearscreen()
        for col in range(self.num_columns):
            for row in range(self.num_rows):
                if self.grids[self.active_grid][row][col] == 1:
                    color = ALIVE_COLOR
                else:
                    color = DEAD_COLOR
                pygame.draw.circle(self.screen, color, [int(col*CELL_SIZE+(CELL_SIZE/2)),
                                                        int(row*CELL_SIZE+(CELL_SIZE/2))],
                                   int(CELL_SIZE/2),0)
        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            # if event is keypress "s" pause game
            # if event is keyress "r" randomize grid
            # if event is keyress "q" quit grid
            if event.type == pygame.QUIT:
                sys.exit()

    def run(self):
        self.clearscreen()
        millisecond_between_update = (1.0/6.0)*1000.0

        clock = pygame.time.Clock()
        while True:
            self.handle_events()
            #Time checking
            self.update_generation()
            self.draw_grid()
            #cap framerate at 60fps
            clock.tick(MAX_FPS)


if __name__ == '__main__':
    game = LifeGame()
    game.run()
