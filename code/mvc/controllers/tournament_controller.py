from tinydb import TinyDB
from tinydb.queries import Query
from models.tournament import Tournament
from views.tournament_view import TournamentView

db = TinyDB('db.json')
tournaments_table = db.table('tournaments')
User = Query()


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
        elif choice.lower() == "q":
            next = "quit"
        elif choice.lower() == "h":
            next = "homepage"
        else:
            print("invalid value")
            next = "home_tournament"
        return next, None

    @classmethod
    def create_tournament(cls, store, route_params=None):
        data = TournamentView.new_tournament_page(store)
        data["players"] = []
        for player_id in data['player_ids']:
            player = next(p for p in store["players"]
                          if str(p.id) == str(player_id))
            data["players"].append(player)
        del data["player_ids"]
        tournament = Tournament(**data)
        tournaments_table.insert(tournament.to_dict())
        store["curent_tournament"] = tournament
        store["tournaments"].append(tournament)
        return "tournaments_list", None

    @classmethod
    def list_tournament(cls, store, route_params=None):
        choice, tournament_id = TournamentView.tournament_list(
            store["tournaments"]
            )

        if choice == "2":
            return "tournament_detail", tournament_id
        elif choice == "1":
            return "tournament_start", tournament_id
        elif choice == "3":
            return "delete_tournament", tournament_id
        elif choice.lower() == "q":
            next = "quit"
        elif choice.lower() == "h":
            next = "homepage"
        elif choice.lower() == "b":
            return "home_tournament", None
        else:
            print("invalid value")
            next = "tournaments_list"
        return next, None

    @classmethod
    def delete(cls, store, route_params):
        tournaments_table.remove(User.tournament_id == str(route_params))
        TournamentController.refresh_instance(store)

        return "tournaments_list", None

    def refresh_instance(store):
        store["tournaments"] = []
        tournament_instance = []
        for tournament in tournaments_table.all():
            tournament_instance.append(Tournament.from_dict(store, tournament))
        store["tournaments"] = tournament_instance

    @classmethod
    def details_tournament(cls, store, route_params):
        tournament = ()
        for t in store["tournaments"]:
            if str(t.tournament_id) == str(route_params):
                tournament = t

        choice = TournamentView.tournament_details(tournament)

        if choice == "q":
            return "quit", None
        elif choice == "h":
            return "homepage", None
        elif choice == "b":
            return "tournaments_list", None
        else:
            print("invalid value")
            return "tournament_detail", tournament.tournament_id

    @classmethod
    def start_tournament(cls, store, route_params):
        tournament = next(t for t in store["tournaments"]
                          if str(t.tournament_id) == str(route_params))
        if not tournament.rounds:
            tournament.start_round()
        if tournament.rounds[-1].finished(
        ) and not tournament.finished_tournament():
            tournament.start_other_round()

        tournament_query = Query()
        tournaments_table.update(tournament.to_dict(),
                                 tournament_query.tournament_id
                                 == str(route_params))

        choice, extra_info = TournamentView.start_tournament_page(tournament)

        if len(tournament.rounds) < 5:
            if choice == 1:
                tournament.set_winner(extra_info,
                                      tournament.rounds[-1].games[0])
            elif choice == 2:
                tournament.set_winner(extra_info,
                                      tournament.rounds[-1].games[1])
            elif choice == 3:
                tournament.set_winner(extra_info,
                                      tournament.rounds[-1].games[2])
            elif choice == 4:
                tournament.set_winner(extra_info,
                                      tournament.rounds[-1].games[3])
            elif choice.lower() == "q":
                return "quit", None
            elif choice.lower() == "h":
                return "homepage", None
            elif choice.lower() == "b":
                return "tournaments_list", None
            elif choice == "alpha":
                tournament.players = sorted(tournament.players,
                                            key=lambda x: (x.lastname))
                return "tournament_start", tournament.tournament_id
            elif choice == "rank":
                tournament.players = sorted(tournament.players,
                                            key=lambda x: (int(x.ranking)),
                                            reverse=True)
                return "tournament_start", tournament.tournament_id
            else:
                print("invalid value ")
                return "tournament_start", tournament.tournament_id
            return "tournament_start", tournament.tournament_id

        if choice.lower() == "q":
            return "quit", None
        elif choice.lower() == "h":
            return "homepage", None
        elif choice.lower() == "b":
            return "tournaments_list", None

        else:
            print("invalid value")
            next_ = "tournament_start"

        choice, extra_info = TournamentView.start_tournament_page(tournament)
        return next_, None
