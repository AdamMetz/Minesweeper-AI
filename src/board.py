import pygame
import constants
import random
from tile import Tile

class Board:
    def __init__(self):
        self.tiles = [[]]
        self.initialize_board()
    
    # Getters
    def get_tiles(self) -> list:
        return self.tiles

    def initialize_board(self):
        self.generate_board()
        self.bomb_generation()
        self.set_neighbours()
        self.draw_board()

    # Generates the default game board. Board object that contains a list of Tile objects.
    def generate_board(self):
        x = 0
        y = 0
        while x < constants.WIDTH:
            while y < constants.HEIGHT:
                row = constants.WIDTH//constants.IMAGE_PIXEL_WIDTH - (constants.WIDTH-x)//constants.IMAGE_PIXEL_WIDTH
                col = constants.HEIGHT//constants.IMAGE_PIXEL_WIDTH - (constants.HEIGHT-y)//constants.IMAGE_PIXEL_WIDTH
                self.add_tile(Tile(x, y, row, col))
                y += constants.IMAGE_PIXEL_WIDTH            
            x += constants.IMAGE_PIXEL_WIDTH
            y = 0
        pygame.display.update()

    def add_tile(self, tile):
        # Add another row to tiles when needed.          Prevent extra row being added on final iteration.
        if (tile.get_col()+1 == constants.WIDTH//constants.IMAGE_PIXEL_WIDTH) and (tile.get_row()+1 != constants.HEIGHT//constants.IMAGE_PIXEL_WIDTH):
            self.tiles.append([])
        self.tiles[tile.row].append(tile)

    # Randomly selects tiles to be a bomb.
    def bomb_generation(self):
        #num_of_tiles = (constants.HEIGHT//constants.IMAGE_PIXEL_WIDTH)**2
        remaining_bombs = constants.NUM_OF_BOMBS
        board_row_max_index = len(self.get_tiles()) - 1
        board_col_max_index = len(self.get_tiles()[0]) - 1

        while remaining_bombs:
            random_tile_row_index = random.randint(0, board_row_max_index)
            random_tile_col_index = random.randint(0, board_col_max_index)

            if not self.get_tiles()[random_tile_row_index][random_tile_col_index].get_is_bomb():
                self.get_tiles()[random_tile_row_index][random_tile_col_index].set_is_bomb(True)
                remaining_bombs -= 1

    # Sets the neighbours for each Tile.
    def set_neighbours(self):
        board_row_max_index = len(self.get_tiles()) - 1
        board_col_max_index = len(self.get_tiles()[0]) - 1
        for row in self.get_tiles():
            for tile in row:
                curr_tile_row = tile.get_row()
                curr_tile_col = tile.get_col()
                
                #   Here is how each Tile is going to be assessed, with (x_offset=0, y_offset=0) being the Tile being assesed.
                #   (-1, 1)  (0, 1)  (1, 1)
                #   (-1, 0)  (0, 0)  (1, 0)
                #   (-1, -1) (0, -1) (1, -1)
                #   Check if the Tiles surrounding (x_offset=0, y_offset=0) exist, if so add them to Tile.neighbours
                for x_offset in range(-1, 2):
                    for y_offset in range(-1, 2):
                        # x=0, and y=0, is the Tile being checked. 
                        if x_offset or y_offset:
                            # Ensure the neighbouring Tile being checked for exists:
                            # 1. Row and Col index are > 0
                            # 2. Row and Col index are less than their respective max index
                            if (
                            curr_tile_row + x_offset >= 0 
                            and curr_tile_col + y_offset >= 0 
                            and curr_tile_row + x_offset <= board_row_max_index 
                            and curr_tile_col + y_offset <= board_col_max_index):
                                neighbours = tile.get_neighbours()
                                neighbours.append(self.get_tiles()[curr_tile_row + x_offset][curr_tile_col + y_offset])
                                tile.set_neighbours(neighbours)
                                if self.get_tiles()[curr_tile_row + x_offset][curr_tile_col + y_offset].get_is_bomb():
                                    tile.set_nearby_bombs(tile.get_nearby_bombs() + 1)

    # # Counts and sets the number of nearby bombs for each non-bomb Tile.
    # def count_nearby_bombs(self):
    #     for row in self.get_tiles():
    #         for tile in row:
    #             if not tile.get_is_bomb():
    #                 pass

    # Draws all the images for each tile
    def draw_board(self):
        for row in self.get_tiles():
            for tile in row:
                tile.draw_self()
    
    # Updates the board provided a mouse event.
    # Returns True if the clicked tile was a bomb
    # Returns False otherwise
    def update_board(self, clicked_row, clicked_col, event) -> bool:
        updated_clicked_tile = self.tiles[clicked_row][clicked_col].update_clicked_tile(event)
        if updated_clicked_tile.get_is_bomb() and not updated_clicked_tile.get_marked() and event.button == 1:
            return True
        # If the clicked tile has no nearby bombs, all the nearby safe tiles are automatically uncovered.
        elif updated_clicked_tile.get_nearby_bombs() == 0 and not updated_clicked_tile.get_marked() and event.button == 1:
            self.update_nearby_safe_tiles(updated_clicked_tile)

        return False

    def update_nearby_safe_tiles(self, tile):
        if tile.get_nearby_bombs() == 0 and not tile.get_is_bomb():
            for neighbour in tile.get_neighbours():
                if neighbour.get_clicked() == False:
                    neighbour.set_clicked(True)
                    neighbour.draw_self()
                    self.update_nearby_safe_tiles(neighbour)
