import pygame

class Ship:
    """Class that represents ship controlled by the user"""
    def __init__(self, ai_settings, screen):
        """initialize ship and set its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings

        #Load image
        self.image: pygame.Surface = pygame.image.load("sprites/user_ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start each ship at the bottom and center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Decimal center of ship
        self.center = float(self.rect.centerx)

        #Movement flags.
        self.moving_left = False
        self.moving_right = False

    def blitme(self):
        """Draw ship at the current location."""
        self.screen.blit(self.image, self.rect)

    def update_speed(self, new_speed: float | None) -> None:
        """Updates the speed of the ship measured in pixels"""
        if new_speed is not None:
            self.ai_settings.ship_speed_factor = new_speed

    def increment_speed(self, increment: float | None) -> None:
        """Increments the speed of the ship measured by the given increment"""
        if increment is not None:
            self.ai_settings.ship_speed_factor += increment

    def update(self):
        #Allows the craft to move incrementally by the speed_factor and limits the craft to be within the surface borders
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor

        # Update rect object from self.center.
        self.rect.centerx = int(self.center)
