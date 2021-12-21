import datetime


class Round:
    def __init__(self, name) -> None:
        self.games = []
        self.start_date = datetime.datetime.now()
        self.ended_date = None
        self.name = name

    def finished(self):
        return len(self.games ) == 4 and all(game.winner is not None for game in self.games)
