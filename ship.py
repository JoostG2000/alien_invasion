import pygame

class Ship:
    def __init__(self, screen):
        """initialize ship and set its starting position."""
        self.screen = screen

        #Load image
        self.image: pygame.Surface = pygame.image.load("sprites/user_ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start each ship at the bottom and center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Movement attributes

        #Movement events & flags.
        self.moving_left = False
        self.moving_right = False

        #Speed and acceleration
        self.speed: float = 1.0


    def blitme(self):
        """Draw ship at the current location."""
        self.screen.blit(self.image, self.rect)

    def update_speed(self, new_speed: float | None) -> None:
        """Updates the speed of the ship measured in pixels"""
        if new_speed is not None:
            self.speed = new_speed

    def increment_speed(self, increment: (float | None)) -> None:
        """Increments the speed of the ship measured by the given increment"""
        if increment is not None:
            self.speed += increment

    def update(self):
        if self.moving_right:
            self.rect.centerx += self.speed
        if self.moving_left:
            self.rect.centerx -= self.speed
