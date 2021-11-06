from models.tournament import Tournament


class TournamentView:

    @classmethod
    def home_tournament_page(cls):
        print('---------------------------------------------------'
              '---------------------------')
        print("[                               LET'S PLAY!         "
              "                         ]")
        print('---------------------------------------------------'
              '---------------------------\n')
        print('1. New Tournament')
        print('2. Tournaments in progress               H. Homepage')
        print('3. Ended Tournament                      Q. Exit\n')

        choice = input('Choice:')

        return choice

    @classmethod
    def new_tournament_page(cls, store):
        return Tournament.TournamentValidation(store)
    
    @classmethod
    def add_players_page(cls):
        print('---------------------------------------------------'
              '---------------------------')
        print("[                               ADD PLAYERS         "
              "                         ]")
        print('---------------------------------------------------'
              '---------------------------\n')
        choice = input('Choice:')