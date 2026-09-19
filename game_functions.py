import sys

import pygame

#Import pre-defined settings.
from settings import Settings

#import user-controlled ship module.
from ship import Ship

#Import bullet module
from bullet import Bullet

def check_key_down_events(ai_settings, screen, event, ship, bullets):

    if event.key == pygame.K_SPACE:
        #Create bullet
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)

    elif event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True


def check_key_up_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events( 
        ai_settings: Settings,
        screen: pygame.Surface,
        ship: Ship,
        bullets:pygame.sprite.Group) -> None:
    """Respond to keyboard and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_key_down_events(ai_settings, screen, event, ship, bullets)
        
        elif event.type == pygame.KEYUP:
            check_key_up_events(event, ship)
           


def update_screen(
    ai_settings: Settings,
    screen: pygame.Surface,
    ship: Ship,
    bullets:pygame.sprite.Group
) -> None:
    """Update images on the screen and flip to the new screen."""
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #Redraw bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    pygame.display.flip()