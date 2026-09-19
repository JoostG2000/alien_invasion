import pygame

#Import pre-defined settings.
from settings import Settings

#import user-controlled ship module.
from ship import Ship

#Import game_functions module.
import game_functions as gf

#Import group module
from pygame.sprite import Group

def run_game():
    """Initialize game and create a screen object."""
    print("Running game...")
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Initialize user ship
    ship = Ship(ai_settings, screen)

    #Make a group to store bullets
    bullets: pygame.sprite.Group = Group()
    """Main loop for the game"""
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)

    

run_game()