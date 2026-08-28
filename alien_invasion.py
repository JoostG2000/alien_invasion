import pygame

#Import pre-defined settings.
from settings import Settings

#import user-controlled ship module.
from ship import Ship

#Import game_functions module.
import game_functions as gf

def run_game():
    """Initialize game and create a screen object."""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Initialize user ship
    ship = Ship(screen)

    """Main loop for the game"""
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

run_game()