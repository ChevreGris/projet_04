import datetime


class Round:
    def __init__(self, name) -> None:
        self.games = []
        self.start_date = datetime.datetime.now()
        self.ended_date = None
        self.name = name
