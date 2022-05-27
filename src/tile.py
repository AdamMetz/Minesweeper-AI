import pygame
import game

unclicked_tile_image = pygame.image.load('game-images/tile-background.png')
bomb_image = pygame.image.load('game-images/bomb.png')
flag_image = pygame.image.load('game-images/flag.png')

class Tile:
    def __init__(self, x, y, row, col):
        self.x = x
        self.y = y
        self.row = row
        self.col = col
        self.clicked = False
        self.marked = False
        self.is_bomb = False
        self.neighbours = []
        self.nearby_bombs = 0

    # Setters
    def set_x(self, x: int):
        self.x = x
    
    def set_y(self, y: int):
        self.y = y
    
    def set_row(self, row: int):
        self.row = row
    
    def set_col(self, col: int):
        self.col = col
    
    def set_clicked(self, clicked: bool):
        self.clicked = clicked
    
    def set_marked(self, marked: bool):
        self.marked = marked
    
    def set_is_bomb(self, is_bomb: bool):
        self.is_bomb = is_bomb
    
    def set_neighbours(self, neighbours: list):
        self.neighbours = neighbours

    def set_nearby_bombs(self, nearby_bombs: int):
        self.nearby_bombs = nearby_bombs

    # Getters
    def get_x(self) -> int:
        return self.x
    
    def get_y(self) -> int:
        return self.y

    def get_row(self) -> int:
        return self.row

    def get_col(self) -> int:
        return self.col

    def get_clicked(self) -> bool:
        return self.clicked

    def get_marked(self) -> bool:
        return self.marked

    def get_is_bomb(self) -> bool:
        return self.is_bomb

    def get_neighbours(self) -> list:
        return self.neighbours

    def get_nearby_bombs(self) -> int:
        return self.nearby_bombs

    def draw_self(self):
        # Unclicked and unmarked tile
        if not self.get_clicked() and not self.get_marked():
            game.window.blit(unclicked_tile_image, (self.get_x(), self.get_y()))
        # Left clicked bomb
        elif self.get_clicked() and self.is_bomb:
            game.window.blit(bomb_image, (self.get_x(), self.get_y()))
        # Left clicked non-bomb tile
        elif self.get_clicked() and not self.is_bomb:
            game.window.blit(pygame.image.load('game-images/'+str(self.get_nearby_bombs())+'.png'), (self.get_x(), self.get_y()))
        # Right clicked unclicked and unmarked tile
        elif self.get_marked():
            game.window.blit(flag_image, (self.get_x(), self.get_y()))

    # Returns the updated tile
    def update_clicked_tile(self, event):
        if event.button == 1 and not self.get_marked():
            self.set_clicked(True)
        elif event.button == 3 and not self.get_marked() and not self.get_clicked():
            self.set_marked(True)
        elif event.button == 3 and self.get_marked() and not self.get_clicked():
            self.set_marked(False)
        self.draw_self()

        return self

        
