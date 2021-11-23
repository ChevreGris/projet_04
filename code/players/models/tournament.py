from models.round import Round

class Tournament:

    def __init__(self, tournament_id, name, location, date,
                 time_mode, description, players, spaces) -> None:
        self.tournament_id = tournament_id
        self.name = name
        self.location = location
        self.date = date
        #self.rounds = []
        self.time_mode = time_mode
        self.description = description
        self.players = players
        self.spaces = spaces

    def start_round(self):
        #round = Round("round 1")
        pass
