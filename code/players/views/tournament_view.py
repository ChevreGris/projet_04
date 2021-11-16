from input_validation import InputValidation
from views.player_view import PlayerView
import subprocess as sp


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
        print('2. Start or Continue a Tournament            H. Homepage')
        print('3. See Ended Tournament                      Q. Exit\n')

        choice = input('Choice:')
        return choice

    @classmethod
    def new_tournament_page(cls, store):
        id_input = InputValidation.id_validation()
        name_input = InputValidation.name_validation()
        location_input = InputValidation.location_validation()
        date_input = InputValidation.date_validation()
        time_mode_input = InputValidation.time_mode_validation()
        description_input = InputValidation.description_validation()
        
        sp.call('clear', shell=True)
        PlayerView.player_list(store["players"])

        player1 = InputValidation.id_validation()
        player2 = InputValidation.id_validation()
        player3 = InputValidation.id_validation()
        player4 = InputValidation.id_validation()
        player5 = InputValidation.id_validation()
        player6 = InputValidation.id_validation()
        player7 = InputValidation.id_validation()
        player8 = InputValidation.id_validation()

        players_inputs = [player1, player2, player3, player4, player5, player6, player7, player8]

        return {
            'tournament_id': id_input,
            'name': name_input.upper(),
            'location': location_input,
            'date': date_input,
            'time_mode': time_mode_input,
            'description': description_input,
            'player_ids': players_inputs
        }

    @classmethod
    def tournament_list(cls, tournament):
        print('    ---------------------------------------------------'
              '---------------------------')
        print('    [\tId\tName')
        print('    ---------------------------------------------------'
              '---------------------------')

        for tournaments in tournament:
            print(f'    [\t{tournaments.tournament_id}\t{tournaments.name} {tournaments.location}'
                   f'\t\t\t{tournaments.date}\t{tournaments.time_mode}\t{tournaments.description}    ')
        print('    ---------------------------------------------------'
              '---------------------------\n')
        print('1. Tournament details                        B. Back')
        print('2. Start or Continue a Tournament            H. Homepage')
        print('                                             Q. Exit\n')
        choice = input('Choice:')
        extra_info = None

        while True:
            try:
                if choice == '1':
                    extra_info = input(
                        'Enter Tournament Id to see Details (C. Cancel) :'
                    )
                    if extra_info.lower() == 'c':
                        return 'home_player', None
                    else:
                        return choice, int(extra_info)
                elif choice == '2':
                    extra_info = input(
                        'Enter Tournament Id to Start or Continue the Tournament (C. Cancel) :'
                    )
                    if extra_info.lower() == 'c':
                        return 'home_player', None
                    else:
                        return choice, int(extra_info)
            except ValueError:
                print("invalid value")
            else:
                break

        return choice, extra_info

    @classmethod
    def tournament_recap(cls, tournament):
        print('    ---------------------------------------------------'
              '---------------------------')
        print('    [\tId')
        print('    ---------------------------------------------------'
              '---------------------------')
        print(f'    [\t{tournament.tournament_id}\t{tournament.name} {tournament.location}'
              f'\t\t\t{tournament.date}\t{tournament.time_mode}\t{tournament.description}    ')
        for player in tournament.players:
            print(f'    [\t{player.id} {player.lastname} {player.firstname}'
                  f' {player.birthdate} {player.sex} {player.ranking}')        
        print('    ---------------------------------------------------'
              '---------------------------\n')
        print('B. Back')
        print('H. Homepage')
        print('Q. Exit\n')

        choice = input('Choice:')
        extra_info = None
        
        return choice, extra_info

    @classmethod
    def start_tournament_page(cls):
        print('B. Back')
        print('H. Homepage')
        print('Q. Exit\n')

        choice = input('Choice:')
        extra_info = None
        
        return choice, extra_info
