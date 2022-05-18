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
        self.tiles = []

    def add_tile(self, tile):
        self.tiles.append(tile)

        # Randomly selects tiles to be a bomb.
    def bomb_generation(self):
        num_of_tiles = (HEIGHT//IMAGE_PIXEL_WIDTH)**2
        remaining_bombs = NUM_OF_BOMBS
        while remaining_bombs:
            random_tile = random.randint(0, num_of_tiles-1)
            #print(random_tile)
            if not board.tiles[random_tile].is_bomb:
                board.tiles[random_tile].is_bomb = True
                remaining_bombs -= 1


    # Draws all the images for each tile
    def draw_board(self):
        for tile in board.tiles:
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
    
    def draw_self(self):
        if self.is_bomb:
            window.blit(bomb_image, (self.x, self.y))
        else:
            window.blit(tile_image, (self.x, self.y))


# Generates the default game board. Board object that contains a list of Tile objects.
def generate_board():
    game_board = Board()
    x = 0
    y = 0
    while x < WIDTH:
        while y < HEIGHT:
            row = WIDTH//IMAGE_PIXEL_WIDTH - (WIDTH-x)//IMAGE_PIXEL_WIDTH + 1
            col = HEIGHT//IMAGE_PIXEL_WIDTH - (HEIGHT-y)//IMAGE_PIXEL_WIDTH + 1
            game_board.add_tile(Tile(x, y, row, col))
            y += IMAGE_PIXEL_WIDTH            
        x += IMAGE_PIXEL_WIDTH
        y = 0
    pygame.display.update()
    return game_board


# Initializing Board
board = generate_board()
board.bomb_generation()
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