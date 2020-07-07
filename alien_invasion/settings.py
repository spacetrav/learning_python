class Settings():
    """ a class to store all settings for alien invasion"""

    def __init__(self):
        """ initialize game's static settings""" 
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        # ship settings
        self.ship_limit = 1

        # bullet settings
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 2

        # alien settings
        self.fleet_drop_speed = 10

        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # how quickly the game speeds up after beating a level
        self.speedup_scale_alien = 1.2
        self.speedup_scale = 1

        # how quickly alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ initalize settings that change throughout the game """
        self.ship_speed_factor = 12
        self.bullet_speed_factor = 15
        self.alien_speed_factor = 4

        # fleet_direction of 1 represent right; -1 represents left
        self.fleet_direction = 1

        # scoring
        self.alien_points = 50

    def increase_speed(self):
        """ increase speed settings and alien point values """
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale_alien

        self.alien_points = int(self.alien_points * self.score_scale)