import sys

import pygame

def check_events(screen, square):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, square)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, square)

def check_keyup_events(event, square):
    """Respond to key releases"""
    if event.key == pygame.K_RIGHT:
        pass
    elif event.key == pygame.K_LEFT:
        pass

def check_keydown_events(event, square):
    """Respond to keypresses"""
    if event.key == pygame.K_RIGHT:
        pass
    elif event.key == pygame.K_LEFT:
        pass
    elif event.key == pygame.K_ESCAPE:
        #sys.exit()
        pass

def update_screen(screen, squares):
    """Update images on the screen and flip to the new screen"""
    squares.draw()
    # Make the most recently drawn screen visible
    pygame.display.flip()