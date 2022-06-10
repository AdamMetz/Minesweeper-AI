import pygame
import constants
import game

header_background_image = pygame.image.load('game-images/header.png')
reset_button_image = pygame.image.load('game-images/reset-button.png')
reset_button_width = 80
reset_button_height = 80

pygame.font.init()

text_font = pygame.font.SysFont("monospace", 75)

class Header:
    def __init__(self, remaining_markers_count):
        self.remaining_markers_count = remaining_markers_count

    def initialize_header(self):
        self.draw_header()
        self.draw_reset_button()
        self.draw_marker_counter()

    def draw_header(self):
        game.window.blit(header_background_image, (0, 0))

    def draw_reset_button(self):
        upper_left_reset_button_x = (constants.WINDOW_WIDTH // 2) - (reset_button_width // 2)
        upper_left_reset_button_y = (constants.HEADER_HEIGHT // 2) - (reset_button_height // 2)
        game.window.blit(reset_button_image, (upper_left_reset_button_x, upper_left_reset_button_y))
    
    def draw_marker_counter(self):
        number_display = text_font.render(str(self.remaining_markers_count), 1, (0, 0, 0))
        self.draw_header()
        self.draw_reset_button()
        game.window.blit(number_display, (10, 10))

    def increment_remaining_marker_count(self):
        self.remaining_markers_count += 1
        self.draw_marker_counter()

    def decrement_remaining_marker_count(self):
        self.remaining_markers_count -= 1
        self.draw_marker_counter()