from os import replace
from models.player import Player
from views.player_view import PlayerView


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
            #return{'id': input('New ID:')}
        elif choice.lower() == "2":
            return "home_player", None
        elif choice.lower() == "3":
            return "home_player", None
        elif choice.lower() == "4":
            return "home_player", None
        elif choice.lower() == "5":
            return "home_player", None
        elif choice.lower() == "6":
            return "home_player", None

        elif choice.lower() == "b":
            return "home_player", None
        elif choice.lower() == "h":
            return "homepage", None
        elif choice.lower() == "q":
            return "quit", None
        else:
            print("invalid value")
            return "edit_player", None
