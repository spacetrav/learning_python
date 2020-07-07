import game_functions as gf
class GameStats():
    """ track statistics for alien invasion """

    def __init__(self, ai_settings):
        """ initalize statistics """
        self.ai_settings = ai_settings
        self.reset_stats()

        # start game in an active state
        self.game_active = False

        # high score should never be reset

    def reset_stats(self):
        """ initalize statistics that can change durint the game """
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
        self.high_score = gf.get_high_score()
        