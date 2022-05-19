from sqlite3 import Row
import pygame
import random

WIDTH = 1000
HEIGHT = 1000
NUM_OF_BOMBS = 87

running = True

window = pygame.display.set_mode((WIDTH, HEIGHT));

WHITE = (255, 255, 255)
window.fill(WHITE)

tile_image = pygame.image.load('game_images/tile-background.png')
bomb_image = pygame.image.load('game_images/bomb.png')

IMAGE_PIXEL_WIDTH = 50



class Board:
    def __init__(self):
        self.tiles = [[]]

    def add_tile(self, tile):
        # Add another row to tiles when needed.          Prevent extra row being added on final iteration.
        if (tile.col+1 == WIDTH//IMAGE_PIXEL_WIDTH) and (tile.row+1 != HEIGHT//IMAGE_PIXEL_WIDTH):
            self.tiles.append([])
        self.tiles[tile.row].append(tile)

    # Randomly selects tiles to be a bomb.
    def bomb_generation(self):
        #num_of_tiles = (HEIGHT//IMAGE_PIXEL_WIDTH)**2
        remaining_bombs = NUM_OF_BOMBS
        board_row_max_index = len(self.tiles) - 1
        board_col_max_index = len(self.tiles[0]) - 1

        while remaining_bombs:
            random_tile_row_index = random.randint(0, board_row_max_index)
            random_tile_col_index = random.randint(0, board_col_max_index)

            if not self.tiles[random_tile_row_index][random_tile_col_index].is_bomb:
                self.tiles[random_tile_row_index][random_tile_col_index].is_bomb = True
                remaining_bombs -= 1

    # Sets the neighbours for each Tile.
    def set_neighbours(self):
        board_row_max_index = len(self.tiles) - 1
        board_col_max_index = len(self.tiles[0]) - 1
        for row in self.tiles:
            for tile in row:
                curr_tile_row = tile.row
                curr_tile_col = tile.col
                
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
                                tile.neighbours.append(self.tiles[curr_tile_row + x_offset][curr_tile_col + y_offset])
                                if self.tiles[curr_tile_row + x_offset][curr_tile_col + y_offset].is_bomb:
                                    tile.nearby_bombs += 1


    # Counts and sets the number of nearby bombs for each non-bomb Tile.
    def count_nearby_bombs(self):
        for row in self.tiles:
            for tile in row:
                if not tile.is_bomb:
                    pass


    # Draws all the images for each tile
    def draw_board(self):
        for row in self.tiles:
            for tile in row:
                tile.draw_self()



class Tile:
    def __init__(self, x, y, row, col):
        self.x = x
        self.y = y
        self.row = row
        self.col = col
        # States TBD
        self.state = "unclicked"
        self.is_bomb = False
        self.neighbours = []
        self.nearby_bombs = 0
    
    def draw_self(self):
        # Default
        # if self.is_bomb:
        #     window.blit(bomb_image, (self.x, self.y))
        # else:
        #     window.blit(tile_image, (self.x, self.y))

        # For testing
        if self.is_bomb:
            window.blit(bomb_image, (self.x, self.y))
        else:
            window.blit(pygame.image.load('game_images/'+str(self.nearby_bombs)+'.png'), (self.x, self.y))


# Generates the default game board. Board object that contains a list of Tile objects.
def generate_board():
    game_board = Board()
    x = 0
    y = 0
    while x < WIDTH:
        while y < HEIGHT:
            row = WIDTH//IMAGE_PIXEL_WIDTH - (WIDTH-x)//IMAGE_PIXEL_WIDTH
            col = HEIGHT//IMAGE_PIXEL_WIDTH - (HEIGHT-y)//IMAGE_PIXEL_WIDTH
            game_board.add_tile(Tile(x, y, row, col))
            y += IMAGE_PIXEL_WIDTH            
        x += IMAGE_PIXEL_WIDTH
        y = 0
    pygame.display.update()
    return game_board


# Initializing Board
board = generate_board()
board.bomb_generation()
board.set_neighbours()
board.draw_board()

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            # Terminate game with the Escape key
            if event.key == pygame.K_ESCAPE:
                running = False

    pygame.display.update()