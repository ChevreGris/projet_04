from tinydb import TinyDB
import subprocess as sp
from controllers.home_controller import HomePageController
from controllers.player_controller import PlayerController
from models.player import Player
from models.tournament import Tournament
from controllers.tournament_controller import TournamentController

db = TinyDB('db.json')
players_table = db.table('players')
tournaments_table = db.table('tournaments')

class Application:

    routes = {
        "homepage": HomePageController.dispatch,
        "home_player": PlayerController.home_list,
        "new_player": PlayerController.create,
        "delete_player": PlayerController.delete,
        "edit_player": PlayerController.edit,
        "home_tournament": TournamentController.home_tournament,
        "new_tournament": TournamentController.create_tournament,
        "delete_tournament": TournamentController.delete,
        "tournament_detail": TournamentController.details_tournament,
        "tournaments_list": TournamentController.list_tournament,
        "tournament_start": TournamentController.start_tournament,
    }

    def __init__(self) -> None:
        self.route = "homepage"
        self.exit = False
        self.route_params = None
        
        player_instance = []
        for player in players_table.all():
            player_instance.append(Player.from_dict(player))
        tournament_instance = []
        
        self.store = {
            "players": player_instance,
            "tournaments": tournament_instance,
        }
        
        for tournament in tournaments_table.all():
            tournament_instance.append(Tournament.from_dict(self.store, tournament))

    def run(self):
        while not self.exit:
            # Clear the shell output
            sp.call('clear', shell=True)

            # Get the controller method that should handle our current route
            controller_method = self.routes[self.route]

            # Call the controller method, we pass the store and the route's
            # parameters.
            # Every controller should return two things:
            # - the next route to display
            # - the parameters needed for the next route
            next_route, next_params = controller_method(
                self.store, self.route_params
            )

            # set the next route and input
            self.route = next_route
            self.route_params = next_params

            # if the controller returned "quit" then we end the loop
            if next_route == "quit":
                self.exit = True
