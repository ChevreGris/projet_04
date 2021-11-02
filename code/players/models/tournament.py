class Tournament:
    def __init__(self, tournament_id, name, location, date, turn,
                 time_mode, description, player_1, player_2, player_3,
                 player_4, player_5, player_6, player_7, player_8) -> None:
        self.tournament_id = tournament_id
        self.name = name
        self.location = location
        self.date = date
        self.turn = turn
        self.time_mode = time_mode
        self.description = description
        self.player_1 = player_1
        self.player_2 = player_2
        self.player_3 = player_3
        self.player_4 = player_4
        self.player_5 = player_5
        self.player_6 = player_6
        self.player_7 = player_7
        self.player_8 = player_8
