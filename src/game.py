import pygame
from board import Board
import constants

window = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT));
window.fill(constants.WHITE)

class Game:
    def __init__(self):
        self.board = Board()
        self.game_over = False

    # Getters
    def get_game_over(self) -> bool:
        return self.game_over

    # Setters
    def set_game_over(self, game_over: bool):
        self.game_over = game_over

    def handle_mouse_input(self, event):
        if not self.get_game_over():
            x_click_coordinate, y_click_coordinate = event.pos[0], event.pos[1]
            board_row, board_col = x_click_coordinate//constants.IMAGE_PIXEL_WIDTH, y_click_coordinate//constants.IMAGE_PIXEL_WIDTH
            self.set_game_over(self.board.update_board(board_row, board_col, event))

        if self.get_game_over():
            self.handle_game_over()
    
    def handle_game_over(self):
        print("Game Over")
