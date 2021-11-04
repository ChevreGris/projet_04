import datetime


class Round:
    def __init__(self) -> None:
        self.games = []
        self.start_date = datetime.datetime.now()
        self.ended_date = None
