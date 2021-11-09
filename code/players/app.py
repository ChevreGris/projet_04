import subprocess as sp
from controllers.home_controller import HomePageController
from controllers.player_controller import PlayerController
from models.player import Player
from models.tournament import Tournament
from controllers.tournament_controller import TournamentController


class Application:

    routes = {
        "homepage": HomePageController.dispatch,
        "home_player": PlayerController.home_list,
        "new_player": PlayerController.create,
        "delete_player": PlayerController.delete,
        "edit_player": PlayerController.edit,
        "home_tournament": TournamentController.home_tournament,
        "new_tournament": TournamentController.create_tournament,
        "tournament_recap": TournamentController.recap_tournament,
        #"tournaments_in_progress": ,
        #"ended_tournaments": ,
    }

    def __init__(self) -> None:
        self.route = "homepage"
        self.exit = False
        self.route_params = None
        self.store = {
            "players": [
                Player(1, "PICASSO", "Pablo", "25/10/1881", "M", 994),
                Player(2, "ANGELO", "Michel", "06/03/1475", "M", 2143),
                Player(3, "MOZART", "Amadeus", "25/10/1881", "M", 994),
                Player(4, "BACH", "Jean Sébastien", "06/03/1475", "M", 2143),
                Player(5, "DEBUSSY", "Claude", "25/10/1881", "M", 994),
                Player(6, "SATIE", "Erik", "06/03/1475", "M", 2143),
                Player(7, "CURIE", "Marrie", "25/10/1881", "f", 994),
                Player(8, "DEGAULLE", "Charles", "06/03/1475", "M", 2143),
            ],
            "tournaments": [
                Tournament(1, "Test 1", "Paris", "25/10/2021", "a", "Test description", [1,2,3,4,5,6,7,8]),
                Tournament(2, "Test 2", "Lyon", "275/10/2021", "a", "Test description 2", [5,6,7,8,1,2,3,4])
            ]
        }

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
