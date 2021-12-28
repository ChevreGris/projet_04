from models.round import Round
from models.game import Game


class Tournament:

    def __init__(self, tournament_id, name, location, date,
                 time_mode, description, players) -> None:
        self.tournament_id = tournament_id
        self.name = name
        self.location = location
        self.date = date
        self.rounds = []
        self.time_mode = time_mode
        self.description = description
        self.players = players
        self.scores = {}

    def set_winner(self, winner, game):
        if winner == 1:
            game.winner = game.player1
            self.scores[game.player1.id] = self.scores.get(game.player1.id, 0) + 1
        elif winner == 2:
            game.winner = game.player2
            self.scores[game.player2.id] = self.scores.get(game.player2.id, 0) + 1
        elif winner == 3:
            game.winner = False
            self.scores[game.player1.id] = self.scores.get(game.player1.id, 0) + 0.5
            self.scores[game.player2.id] = self.scores.get(game.player2.id, 0) + 0.5


    def start_round(self):
        for player in self.players:
            self.scores[player.id] = 0

        round = Round("round 1")
        players_by_ranking = sorted(self.players, key=lambda player: (player.ranking), reverse=True)
        groupe1 = players_by_ranking[:4]
        groupe2 = players_by_ranking[4:]
        game1 = Game(groupe1[0], groupe2[0])
        round.games.append(game1)
        game2 = Game(groupe1[1], groupe2[1])
        round.games.append(game2)
        game3 = Game(groupe1[2], groupe2[2])
        round.games.append(game3)
        game4 = Game(groupe1[3], groupe2[3])
        round.games.append(game4)
        self.rounds.append(round)
        pass

    def has_played(self, player1, player2):
        for round in self.rounds:
            for game in round.games:
                if player1 in (game.player1, game.player2) and player2 in (game.player1, game.player2):
                    return True

    def start_other_round(self):
        round = Round(f"Round {len(self.rounds) + 1}")

        for player in self.players:
            player.score = self.scores.get(player.id, 0)
        self.players = sorted(self.players, key=lambda x:(x.score , x.ranking), reverse=True)

        available_players = self.players.copy()
        while available_players:
            curent_player = available_players.pop(0)
            for i, player in enumerate(available_players):
                if not self.has_played(curent_player, player):
                    round.games.append(Game(curent_player, player))
                    del available_players[i]
                    break
        
        self.rounds.append(round)
        pass

    def finished_tournament(self):
        return len(self.rounds) == 4 and self.rounds[3].finished()

