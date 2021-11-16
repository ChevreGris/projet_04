from models.tournament import Tournament
from views.tournament_view import TournamentView


class TournamentController:

    @classmethod
    def home_tournament(cls, store=None, route_params=None):
        choice = TournamentView.home_tournament_page()

        if choice == "1":
            next = "new_tournament"
        elif choice == "2":
            next = "tournaments_list"
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
        data["players"] = []
        for player_id in data['player_ids']:
            player = next(p for p in store["players"] if str(p.id) == str(player_id))
            data["players"].append(player)
        del data["player_ids"]
        tournament = Tournament(**data)
        store["curent_tournament"] = tournament
        store["tournaments"].append(tournament)
        return "home_tournament", None

    @classmethod
    def list_tournament(cls, store, route_params=None):
        choice, tournament_id = TournamentView.tournament_list(store["tournaments"])

        if choice == "1":
            return "tournament_recap", tournament_id
        elif choice == "2":
            return "start_tournament_page", tournament_id
        elif choice == "q":
            next = "quit"
        elif choice == "h":
            next = "homepage"
        elif choice == "b":
            return "home_tournament", None
        else:
            print("invalid value home tournament")
            next = "home_tournament"
        return next, None

    @classmethod
    def recap_tournament(cls, store, route_params):
        tournament = next(t for t in store["tournaments"] if str(t.tournament_id) == str(route_params))
        choice = TournamentView.tournament_recap(tournament)

        if choice == "q":
            next_ = "quit"
        elif choice == "h":
            next_ = "homepage"
        elif choice == "b":
            return "home_tournament", None
        else:
            print("invalid value home tournament")
            next_ = "home_tournament"
        return next_, None

    @classmethod
    def start_tournament(cls, store, route_params):
        choice = TournamentView.start_tournament_page()

        if choice == "q":
            next = "quit"
        elif choice == "h":
            next = "homepage"
        elif choice == "b":
            return "home_tournament", None
        else:
            print("invalid value home tournament")
            next = "home_tournament"
        return next, None
