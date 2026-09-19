import sys

import pygame

#Import pre-defined settings.
from settings import Settings

#import user-controlled ship module.
from ship import Ship

#Import bullet module
from bullet import Bullet


def fire_bullet(ai_settings, screen, ship, bullets):
    """"Create a bullet if the limit is not reached yet."""
    if len(bullets) < ai_settings.max_bullets:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)


def check_key_down_events(ai_settings, screen, event, ship, bullets):
    """Listen for key presses."""
    if event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True



def check_key_up_events(event, ship):
    """Listen for key releases."""
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
            print('Exited game, thanks for playing')
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


def update_bullets(bullets: pygame.sprite.Group):
    """Removes bullets once they are off-screen. """
    bullets.update()
    #Remove bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)