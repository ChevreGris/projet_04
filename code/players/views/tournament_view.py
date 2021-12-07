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
    def start_tournament_page(cls, tournament):
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
        for round in tournament.rounds:
            print('----------------------------------------------------------------------------------------------')
            print(f"[                                      {round.name}                                         ]")
            print('----------------------------------------------------------------------------------------------')
            print('[  Game:  Player Id and Name:                  VS           Player Id and Name:              ]')
            print('[                                                                                            ]')
            for game in round.games:
                print(f'(A)   {game.player1.id} {game.player1.fullname}{game.player1.space}vs             {game.player2.id} {game.player2.fullname}')
            print('----------------------------------------------------------------------------------------------\n')
            print('\n')
        print('1. Game (A)')
        if tournament.rounds[-1].games[0].winner is not None:
            if not tournament.rounds[-1].games[0].winner:
                print('Draw')
            else :
                print(f'    Winner : {tournament.rounds[-1].games[0].winner.fullname}')

        print('2. Game (B)')
        if tournament.rounds[-1].games[1].winner is not None:
            if not tournament.rounds[-1].games[1].winner:
                print('Draw')
            else :
                print(f'    Winner : {tournament.rounds[-1].games[1].winner.fullname}')

        print('3. Game (C)')
        if tournament.rounds[-1].games[2].winner is not None:
            if not tournament.rounds[-1].games[2].winner:
                print('Draw')
            else :
                print(f'    Winner : {tournament.rounds[-1].games[2].winner.fullname}')

        print('4. Game (D)')
        if tournament.rounds[-1].games[3].winner is not None:
            if not tournament.rounds[-1].games[3].winner:
                print('Draw')
            else :
                print(f'    Winner : {tournament.rounds[-1].games[3].winner.fullname}\n')

        print('B. Back')
        print('H. Homepage')
        print('Q. Exit\n')
        
        
        choice = input('Choice: ')
        if choice in "1234":
            choice = int(choice)
        extra_info = None

        while True:
            try:
                extra_info = input(
                    f'1. {round.games[choice -1].player1.fullname}\n'
                    f'2. {round.games[choice -1].player2.fullname}\n'
                    '3. draw\n'
                    'Enter winner  ("C" to cancel): '
                    )   
                if extra_info.lower() == 'c':
                    return 'tournament_start', None
                else:
                    return choice, int(extra_info)
            except ValueError:
                print("invalid value")
            else:
                break
            return choice, extra_info

    