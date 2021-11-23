from input_validation import InputValidation
from views.player_view import PlayerView
import subprocess as sp


class TournamentView:

    @classmethod
    def home_tournament_page(cls):
        print('Home Tournament \n')
        print('1. New Tournament')
        print('2. Tournament list')
        print('3. See Ended Tournament\n')
        print('H. Homepage')
        print('Q. Exit\n')


        choice = input('Choice: ')
        return choice

    @classmethod
    def new_tournament_page(cls, store):
        id_input = InputValidation.id_validation()
        name_input = InputValidation.name_validation()
        location_input = InputValidation.location_validation()
        date_input = InputValidation.date_validation()
        time_mode_input = InputValidation.time_mode_validation()
        description_input = InputValidation.description_validation()
        spaces = InputValidation.lenght_to_max(name_input, location_input)
        
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
            'player_ids': players_inputs,
            'spaces' : spaces,
        }

    @classmethod
    def tournament_list(cls, tournament):
        print('----------------------------------------------------------------------------------------------')
        print("[                                      TOURNAMENT LIST                                       ]")
        print('----------------------------------------------------------------------------------------------')
        print("[                                                                                            ]")
        print('[             ID      Name, Location                       Date         Time mode            ]')
        print("[                                                                                            ]")
        for tournaments in tournament:
            print(f'[             {tournaments.tournament_id}       {tournaments.name}, {tournaments.location}{tournaments.spaces}  {tournaments.date}          {tournaments.time_mode}                ]')
        print("[                                                                                            ]")
        print('----------------------------------------------------------------------------------------------\n')
        print('    1. Start or Continue a Tournament            B. Back')
        print('    2. Tournament details                        H. Homepage')
        print('                                                 Q. Exit\n')
        choice = input('Choice: ')
        extra_info = None

        while True:
            try:
                if choice == '2':
                    extra_info = input(
                        'Enter Tournament Id to see Details (C. Cancel): '
                    )
                    if extra_info.lower() == 'c':
                        return 'home_player', None
                    else:
                        return choice, int(extra_info)
                elif choice == '1':
                    extra_info = input(
                        'Enter Tournament Id to Start or Continue the Tournament (C. Cancel): '
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
    def tournament_details(cls, tournament):
        print('----------------------------------------------------------------------------------------------')
        print("[                                   TOURNAMENT DESCRIPTION                                   ]")
        print('----------------------------------------------------------------------------------------------\n')
        print(f'    ID : {tournament.tournament_id}')
        print(f'    Name : {tournament.name}')
        print(f'    Location : {tournament.location}')
        print(f'    Date : {tournament.date}')
        print(f'    Time Mode : {tournament.time_mode}')
        print(f'    Description : {tournament.description}\n')
        print('    Players :')
        PlayerView.player_list(tournament.players)
        print('B. Back')
        print('H. Homepage')
        print('Q. Exit\n')

        choice = input('Choice: ')
        extra_info = None
        
        return choice, extra_info

    @classmethod
    def start_tournament_page(cls, tournament, players_by_ranking):
        print('----------------------------------------------------------------------------------------------')
        print("[                                   TOURNAMENT DESCRIPTION                                   ]")
        print('----------------------------------------------------------------------------------------------\n')
        print(f'    ID : {tournament.tournament_id}')
        print(f'    Name : {tournament.name}')
        print(f'    Location : {tournament.location}')
        print(f'    Date : {tournament.date}')
        print(f'    Time Mode : {tournament.time_mode}')
        print(f'    Description : {tournament.description}\n')
        print('    Players :')
        PlayerView.player_list(tournament.players)
        print('')

        print('----------------------------------------------------------------------------------------------')
        print("[                                        FIRST ROUND                                         ]")
        print('----------------------------------------------------------------------------------------------')
        print('[  Game:  Player Id and Name:                  VS           Player Id and Name:              ]')
        print('[                                                                                            ]')
        print(f'[   (A)   {players_by_ranking[0].id} {players_by_ranking[0].lastname} {players_by_ranking[0].firstname}{players_by_ranking[0].space}    /            {players_by_ranking[0].id} {players_by_ranking[1].lastname} {players_by_ranking[1].firstname}{players_by_ranking[1].space}]')
        print(f'[   (B)   {players_by_ranking[2].id} {players_by_ranking[2].lastname} {players_by_ranking[2].firstname}{players_by_ranking[2].space}    /            {players_by_ranking[3].id} {players_by_ranking[3].lastname} {players_by_ranking[3].firstname}{players_by_ranking[3].space}]')
        print(f'[   (C)   {players_by_ranking[4].id} {players_by_ranking[4].lastname} {players_by_ranking[4].firstname}{players_by_ranking[4].space}    /            {players_by_ranking[5].id} {players_by_ranking[5].lastname} {players_by_ranking[5].firstname}{players_by_ranking[5].space}]')
        print(f'[   (D)   {players_by_ranking[6].id} {players_by_ranking[6].lastname} {players_by_ranking[6].firstname}{players_by_ranking[6].space}    /            {players_by_ranking[7].id} {players_by_ranking[7].lastname} {players_by_ranking[7].firstname}{players_by_ranking[7].space}]')
        print('[                                                                                            ]')
        print('----------------------------------------------------------------------------------------------\n')
        print('\n')
        print('1. Game (A)')
        print('2. Game (B)')
        print('3. Game (C)')
        print('4. Game (D)\n')
        print('B. Back')
        print('H. Homepage')
        print('Q. Exit\n')
        
        choice = input('Choice: ')
        extra_info = None

        while True:
            try:
                if choice == '1':
                    extra_info = input(
                        'Enter winner ID (enter "NULL" for draw, "C" to cancel): '
                    )
                    if extra_info.lower() == 'null':
                        return choice, extra_info
                    elif extra_info.lower() == 'c':
                        return 'tournament_start', None
                    else:
                        return choice, int(extra_info)
                elif choice == '2':
                    extra_info = input(
                        'Enter winner ID (enter "NULL" for draw, "C" to cancel): '
                    )
                    if extra_info.lower() == 'null':
                        return choice, extra_info
                    elif extra_info.lower() == 'c':
                        return 'tournament_start', None
                    else:
                        return choice, int(extra_info)
                elif choice == '3':
                    extra_info = input(
                        'Enter winner ID (enter "NULL" for draw, "C" to cancel): '
                    )
                    if extra_info.lower() == 'null':
                        return choice, extra_info
                    elif extra_info.lower() == 'c':
                        return 'tournament_start', None
                    else:
                        return choice, int(extra_info)
                elif choice == '4':
                    extra_info = input(
                        'Enter winner ID (enter "NULL" for draw, "C" to cancel): '
                    )
                    if extra_info.lower() == 'null':
                        return choice, extra_info
                    elif extra_info.lower() == 'c':
                        return 'tournament_start', None
                    else:
                        return choice, int(extra_info)
            except ValueError:
                print("invalid value")
            else:
                break

        return choice, extra_info
