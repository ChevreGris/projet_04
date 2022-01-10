from datetime import datetime
from models.game import Game


class Round:
    def __init__(self, name) -> None:
        self.games = []
        self.start_time = datetime.now()
        self.ended_time = None
        self.name = name

    def to_dict(self):
        games = []
        for game in self.games:
            games.append(Game.to_dict(game))
        str_start_time = self.start_time.strftime(
            "%m/%d/%Y, %H:%M:%S"
        ) if self.start_time else None
        str_ended_time = self.ended_time if self.ended_time else None

        return {
            'start_time': str_start_time,
            'ended_time': str_ended_time,
            'name': self.name,
            'games': games
        }

    @classmethod
    def from_dict(cls, store, game_dict):
        rounds = []
        for r in game_dict:
            round = Round(r['name'])
            round.start_time = datetime.strptime(
                r['start_time'], '%m/%d/%Y, %H:%M:%S'
            ) if r['start_time'] else None
            round.ended_time = datetime.strptime(
                r['ended_time'], '%m/%d/%Y, %H:%M:%S'
            ) if r['ended_time'] else None
            round.games = Game.from_dict(store, r['games'])
            rounds.append(round)
        return rounds

    def finished(self):
        return all(game.winner is not None for game in self.games)
