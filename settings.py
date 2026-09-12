class Settings:
    """A class containing all settings for the game"""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (24, 30, 76)

        #Speed and acceleration
        self.ship_speed_factor: float = 3

        #bullet char
        self.bullet_speed_factor = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
                