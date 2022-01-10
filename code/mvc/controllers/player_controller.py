from tinydb import TinyDB
from tinydb.queries import Query
from models.player import Player
from views.player_view import PlayerView
from input_validation import InputValidation

db = TinyDB('db.json')
players_table = db.table('players')
User = Query()


class PlayerController:
    @classmethod
    def home_list(cls, store, route_params=None):
        choice, player_id = PlayerView.home_player_list(store["players"])

        if choice == "1":
            return "new_player", None
        elif choice == "2":
            return "edit_player", player_id
        elif choice == "3":
            return "delete_player", player_id
        elif choice == "q":
            return "quit", None
        elif choice.lower() == "h":
            return "homepage", None
        elif choice.lower() == "a":
            store["players"] = sorted(store["players"],
                                      key=lambda x: (x.lastname))
            return "home_player", None
        elif choice.lower() == "r":
            store["players"] = sorted(store["players"],
                                      key=lambda x: (int(x.ranking)),
                                      reverse=True)
            return "home_player", None
        elif choice.lower() == "i":
            store["players"] = sorted(store["players"],
                                      key=lambda x: (int(x.id)))
            return "home_player", None
        else:
            print("invalid value ")
            return "home_player", None

    @classmethod
    def create(cls, store, route_params=None):
        data = PlayerView.create_player()
        player = Player(**data)
        players_table.insert(player.to_dict())
        store["players"].append(player)
        return "home_player", None

    def refresh_instance(store):
        store["players"] = []
        player_instance = []
        for player in players_table.all():
            player_instance.append(Player.from_dict(player))
        store["players"] = player_instance

    @classmethod
    def delete(cls, store, route_params):
        players_table.remove(User.id == str(route_params))
        PlayerController.refresh_instance(store)

        return "home_player", None

    @classmethod
    def edit(cls, store, route_params):
        for p in store["players"]:
            if str(p.id) == str(route_params):
                player = p
            else:
                pass

        choice = PlayerView.edit_player(player)

        if choice.lower() == "1":
            lastname_input = InputValidation.lastname_validation()
            players_table.update({"lastname": lastname_input},
                                 User.id == str(route_params))
            PlayerController.refresh_instance(store)
            return "edit_player", route_params
        elif choice.lower() == "2":
            firstname_input = InputValidation.firstname_validation()
            players_table.update({"firstname": firstname_input},
                                 User.id == str(route_params))
            PlayerController.refresh_instance(store)
            return "edit_player", route_params
        elif choice.lower() == "3":
            birthdate_input = InputValidation.birthdate_validation()
            players_table.update({"birthdate": birthdate_input},
                                 User.id == str(route_params))
            PlayerController.refresh_instance(store)
            return "edit_player", route_params
        elif choice.lower() == "4":
            sex_input = InputValidation.sex_validation()
            players_table.update({"sex": sex_input},
                                 User.id == str(route_params))
            PlayerController.refresh_instance(store)
            return "edit_player", route_params
        elif choice.lower() == "5":
            ranking_input = InputValidation.ranking_validation()
            players_table.update({"ranking": ranking_input},
                                 User.id == str(route_params))
            PlayerController.refresh_instance(store)
            return "edit_player", route_params

        elif choice.lower() == "b":
            return "home_player", None
        elif choice.lower() == "h":
            return "homepage", None
        elif choice.lower() == "q":
            return "quit", None
        else:
            print("invalid value")
            return "edit_player", route_params
