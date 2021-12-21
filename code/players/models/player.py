class Player:
    def __init__(self, id, lastname, firstname, birthdate, sex, ranking) -> None:
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
        return{'id' : self.id, 'lastname' : self.lastname}

    def __repr__(self) -> str:
        return f'{self.id} {self.ranking} {self.score}'
