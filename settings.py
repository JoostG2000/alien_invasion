class Settings:
    """A class containing all settings for the game"""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (24, 30, 76)

        # Speed and acceleration
        self.ship_speed_factor: float = 1

        # Bullet settings
        self.bullet_speed_factor = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 127, 0
        self.max_bullets = 3
