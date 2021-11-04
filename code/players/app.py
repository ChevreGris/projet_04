from controllers.home_controller import HomePageController
from models.player import Player
from controllers.player_controller import PlayerController
import subprocess as sp


class Application:

    routes = {
        "homepage": HomePageController.dispatch,
        "home_player": PlayerController.home_list,
        "new_player": PlayerController.create,
        "delete_player": PlayerController.delete,
        "edit_player": PlayerController.edit,
    }

    def __init__(self) -> None:
        self.route = "homepage"
        self.exit = False
        self.route_params = None
        self.store = {
            "players": [
                Player(1, "PICASSO", "Pablo", "25/10/1881", "M", 994),
                Player(2, "ANGELO", "Michel", "06/03/1475", "M", 2143),
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
