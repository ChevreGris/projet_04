import datetime
from models.game import Game


class Round:
    def __init__(self, name) -> None:
        self.games = []
        self.start_time = datetime.datetime.now()
        self.ended_time = None
        self.name = name
    

    def to_dict(self):
        games = []
        for game in self.games:
            games.append(Game.to_dict(game))

        return {
            'start_time': self.start_time,
            'ended_time': self.ended_time,
            'name': self.name,
            'games': games

        }

    def finished(self):
        return len(self.games ) == 4 and all(game.winner is not None for game in self.games)
