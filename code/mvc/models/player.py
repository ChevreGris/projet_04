class Player:
    def __init__(self,
                 id,
                 lastname,
                 firstname,
                 birthdate,
                 sex,
                 ranking) -> None:
        self.id = id
        self.lastname = lastname
        self.firstname = firstname
        self.birthdate = birthdate
        self.sex = sex
        self.ranking = ranking

    @property
    def fullname(self):
        return f'{self.firstname} {self.lastname.upper()}'

    def to_dict(self):
        return {
                 'id': self.id,
                 'lastname': self.lastname,
                 'firstname': self.firstname,
                 'birthdate': self.birthdate,
                 'sex': self.sex,
                 'ranking': self.ranking
                 }

    @classmethod
    def from_dict(cls, player_dict):
        return Player(player_dict['id'], player_dict['lastname'],
                      player_dict['firstname'], player_dict['birthdate'],
                      player_dict['sex'], player_dict['ranking'])

    def __repr__(self) -> str:
        return f'{self.id} {self.ranking} {self.score}'
