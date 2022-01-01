class Game:
    def __init__(self, player1, player2 ) -> None:
        self.player1 = player1
        self.player2 = player2
        self.winner = None

    def to_dict(self):
        return {
            'player1': self.player1,
            'player2': self.player2,
            'winner': self.winner
        }
