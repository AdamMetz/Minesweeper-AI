import pygame
from game import Game
import constants

running = True

# Game initialization
game = Game()

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            # Terminate game with the Escape key
            if event.key == pygame.K_ESCAPE:
                running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            game.handle_mouse_input(event)

    pygame.display.update()