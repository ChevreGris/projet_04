from models.player import Player
from views.player_view import PlayerView
from input_validation import InputValidation


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
        else:
            print("invalid value ")
            return "home_player", None

    @classmethod
    def create(cls, store, route_params=None):
        data = PlayerView.create_player()
        player = Player(**data)
        store["players"].append(player)
        return "home_player", None

    @classmethod
    def delete(cls, store, route_params):
        store["players"] = [
            p for p in store["players"] if p.id != route_params
        ]
        return "home_player", None

    @classmethod
    def edit(cls, store, route_params):
        player = next(p for p in store["players"] if p.id == route_params)
        choice = PlayerView.edit_player(player)
        
        if choice.lower() == "1":
            id_input = InputValidation.id_validation()
            return{'id': id_input}
        elif choice.lower() == "2":
            lastname_input = InputValidation.lastname_validation()
            return{'lastname': lastname_input.upper()}
        elif choice.lower() == "3":
            firstname_input = InputValidation.firstname_validation()
            return{'firstname': firstname_input.capitalize()}
        elif choice.lower() == "4":
            birthdate_input = InputValidation.birthdate_validation()
            return{'birthdate': birthdate_input}
        elif choice.lower() == "5":
            sex_input = InputValidation.sex_validation()
            return{'sex': sex_input.upper()}
        elif choice.lower() == "6":
            ranking_input = InputValidation.ranking_validation()
            return{'ranking': ranking_input}

        elif choice.lower() == "b":
            return "home_player", None
        elif choice.lower() == "h":
            return "homepage", None
        elif choice.lower() == "q":
            return "quit", None
        else:
            print("invalid value")
            return "edit_player", None
