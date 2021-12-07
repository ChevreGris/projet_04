
from models.round import Round
from models.game import Game


class Tournament:

    def __init__(self, tournament_id, name, location, date,
                 time_mode, description, players, spaces) -> None:
        self.tournament_id = tournament_id
        self.name = name
        self.location = location
        self.date = date
        self.rounds = []
        self.time_mode = time_mode
        self.description = description
        self.players = players
        self.spaces = spaces
        self.scores = {}

    def set_winner(self, winner, game):
        if winner == 1:
            id = game.player1.id
            ranking = game.player1.ranking
            curent_points = self.scores[id][1]
            self.scores.update({id: [ranking, curent_points + 1]})
            game.winner = game.player1
            print(self.scores)
        elif winner == 2:
            id = game.player2.id
            ranking = game.player2.ranking
            curent_points = self.scores[id][1]
            self.scores.update({id: [ranking, curent_points + 1]})
            game.winner = game.player2
            print(self.scores)
        if winner == 3:
            id = game.player1.id
            ranking = game.player1.ranking
            curent_points = self.scores[id][1]
            self.scores.update({id: [ranking, curent_points + 0.5]})
            id2 = game.player2.id
            ranking2 = game.player2.ranking
            curent_points2 = self.scores[id2][1]
            self.scores.update({id2: [ranking2, curent_points2 + 0.5]})
            game.winner = False
            print(self.scores)


    def start_round(self):
        round = Round("round 1")
        for player in self.players:
            self.scores[player.id] = [player.ranking, 0]
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
            for game in round.matches:
                if player1 in (game.player1, game.player2) and player2 in (game.player1, game.player2):
                    return True

    def start_other_round(self):
        round = Round(f"Round {len(self.rounds) + 1}")
        score_by_order = sorted(self.scores.items(), key=lambda kv: (kv[1][1], kv[1]), reverse=True)
        order_by_id = []
        for id in score_by_order:
            order_by_id.append(id[0])
        players_by_order = sorted(self.players, key=lambda x: order_by_id.index(x[0]))
        #players_by_order.sort(key=lambda x: order_by_id.index(x[0]))

        print(score_by_order)
        print(order_by_id)
        print(players_by_order)
        i = input('i')
        self.rounds.append(round)
        pass

