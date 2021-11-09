from models.tournament import Tournament
from views.tournament_view import TournamentView


class TournamentController:

    @classmethod
    def home_tournament(cls, store=None, route_params=None):
        choice = TournamentView.home_tournament_page()

        if choice == "1":
            next = "new_tournament"
        elif choice == "2":
            next = "tournaments_in_progress"
        elif choice == "3":
            next = "ended_tournament"
        elif choice == "q":
            next = "quit"
        elif choice == "h":
            next = "homepage"
        else:
            print("invalid value home tournament")
            next = "home_tournament"
        return next, None

    @classmethod
    def create_tournament(cls, store, route_params=None):
        data = TournamentView.new_tournament_page(store)
        tournament = Tournament(**data)
        store["tournaments"].append(tournament)
        return "tournament_recap", tournament.tournament_id
    
    @classmethod
    def recap_tournament(cls, store, route_params):
        tournament = next(t for t in store["tournaments"] if t.tournament_id == route_params)
        TournamentView.tournament_recap(tournament, store["players"])
        #return "homepage", None

