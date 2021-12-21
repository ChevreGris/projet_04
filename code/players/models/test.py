
from tinydb import TinyDB, Query

class Player:
    def __init__(self, id, lastname, firstname, birthdate, sex, ranking, space) -> None:
        self.id = id
        self.lastname = lastname
        self.firstname = firstname
        self.birthdate = birthdate
        self.sex = sex
        self.ranking = ranking
        self.space = space

    @property
    def fullname(self):
        return f'{self.firstname} {self.lastname.upper()}'
    
    def to_dict(self):
        return{'id' : self.id, 'lastname' : self.lastname}

db = TinyDB('db.json')
player = Player(1, "PICASSO", "Pablo", "25/10/1881", "M", 994, "                  ")
print(db.insert(player.to_dict()))

