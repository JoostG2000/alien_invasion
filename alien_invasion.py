## Import pygame modules
import pygame
from pygame.sprite import Group


#Import pre-defined settings and functions.
from settings import Settings
import game_functions as gf


#import user-controlled ship module and alien module.
from ship import Ship
from aliens import Alien



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

    #Initialize aliens
    alien = Alien(ai_settings, screen)


    #Make a group to store bullets
    bullets: pygame.sprite.Group = Group()
    """Main loop for the game"""
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, alien, bullets)

    

run_game()