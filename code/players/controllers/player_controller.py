from models.player import Player
from views.player_view import PlayerView


class PlayerController:

    @classmethod
    def list(cls, store, route_params=None):
        choice, player_id = PlayerView.display_list(store["players"])

        if choice == "1":
            return "view_player", player_id
        elif choice == "2":
            return "new_player", None
        elif choice == "3":
            return "delete_player", player_id
        elif choice == "4":
            return "quit", None
        elif choice.lower() == "h":
            return "homepage", None
        else:
            print("invalid value")
            return "list_player", None

    @classmethod
    def create(cls, store, route_params=None):

        data = PlayerView.create_player()
        player = Player(**data)
        store["players"].append(player)

        return "list_player", None

    @classmethod
    def delete(cls, store, route_params):
        # remove the player from the store
        store["players"] = [
            p for p in store["players"] if p.id != route_params
        ]
        return "list_player", None

    @classmethod
    def view(cls, store, route_params):
        """
        Display one single player, the route_params correspond to the player ID
        we want to display
        """
        # search the player on the store
        player = next(p for p in store["players"] if p.id == route_params)

        # we pass the player to the view that will display the player info and
        # the next options
        choice = PlayerView.detail_player(player)
        if choice.lower() == "q":
            return "quit", None
        elif choice.lower() == "h":
            return "homepage", None
        elif choice == "1":
            return "edit_player", None
        else:
            print("invalid value")
            return "view_player", None
    
    @classmethod
    def edit(cls, store=None, route_params=None):
        choice = PlayerView.edit_player()
        if choice.lower() == "q":
            return "quit", None
        elif choice.lower() == "h":
            return "homepage", None
        else:
            print("invalid value")
            return "edit_player", None