import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_settings, screen):
            """initialize the alien and set its starting position."""
            super(Sprite).__init__()
            self.screen = screen
            self.ai_settings = ai_settings
    
            #Load image
            self.image: pygame.Surface = pygame.image.load("sprites/alien_fighter.bmp")
            self.rect = self.image.get_rect()
            
    
            #Start each ship at the top left
            self.rect.x = self.rect.width
            self.rect.y = self.rect.height
    
            #Decimal center of ship
            self.x = float(self.rect.x)
    
            #Movement flags.
            self.moving_left = False
            self.moving_right = False
    
    def blitme(self):
        """Draw the alien at the current location."""
        self.screen.blit(self.image, self.rect)
