class Game:
    def __init__(self, player1, player2) -> None:
        self.player1 = player1
        self.player2 = player2
        self.winner = None

    def to_dict(self):
        if self.winner is None:
            id = self.winner
        elif self.winner is False:
            id = False
        else:
            id = self.winner.id

        return {
            'player1': self.player1.id,
            'player2': self.player2.id,
            'winner': id
        }

    @classmethod
    def from_dict(cls, store, game_dict):
        games = []
        winner = None
        player1 = None
        player2 = None
        for g in game_dict:
            for p in store["players"]:
                if str(p.id) == str(g['player1']):
                    player1 = p
                if str(p.id) == str(g['player2']):
                    player2 = p
                if str(p.id) == str(g['winner']):
                    winner = p
                elif g['winner'] is None:
                    winner = None
                elif g['winner'] is False:
                    winner = False

            game = Game(player1=player1, player2=player2)
            game.winner = winner
            games.append(game)

        return games
