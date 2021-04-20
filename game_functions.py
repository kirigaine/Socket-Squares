import sys

import pygame

def check_events(screen, square):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("justquit")
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, square)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, square)

def update_screen(screen, squares, player_squares):
    """Update images on the screen and flip to the new screen"""

    squares.update()
    screen.fill((0,0,0))
    for squa in player_squares:
        if squa is not None and squa.player_id != squares.player_id:
            squa.screen = screen
            squa.draw()
    squares.draw()
    # Make the most recently drawn screen visible
    pygame.display.flip()

def check_keydown_events(event, square):
    """Respond to keypresses"""
    if event.key == pygame.K_ESCAPE:
        print("escape")
        sys.exit()  
    elif event.key == pygame.K_UP or event.key == pygame.K_w:
        square.y_velocity -= 3
    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
        square.y_velocity += 3
    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        square.h_velocity += 3
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        square.h_velocity -= 3

def check_keyup_events(event, square):
    """Respond to key releases"""
    if event.key == pygame.K_UP or event.key == pygame.K_w:
        square.y_velocity += 3
    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
        square.y_velocity -= 3
    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        square.h_velocity -= 3
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        square.h_velocity += 3
