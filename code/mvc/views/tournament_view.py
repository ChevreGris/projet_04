from input_validation import InputValidation
from views.player_view import PlayerView
from views.home_view import HomeView
import subprocess as sp


def space(player):
    # set the space betwin name and date in player menu
    max_lenght = 30 - len(player.lastname + player.firstname)
    return " " * max_lenght


def space_town(tournaments):
    max_lenght = 20 - len(tournaments.location)
    return " " * max_lenght


def space_name(tournaments):
    max_lenght = 20 - len(tournaments.name)
    return " " * max_lenght


def space_id(tournaments):
    max_lenght = 4 - len(str(tournaments.tournament_id))
    return " " * max_lenght


def win(winner, player):
    if winner is None:
        return' '
    if winner is False:
        return'♦︎'
    elif winner.id == player.id:
        return'♦︎'
    else:
        return' '


class TournamentView:

    @classmethod
    def home_tournament_page(cls):
        HomeView.chess_title()
        print('    Home Tournament \n')
        print('    1. New Tournament                            H. Homepage')
        print('    2. Tournament list                           Q. Exit\n')

        choice = input('    Choice: ')
        return choice

    def print_name(store, player1):
        for p in store["players"]:
            if str(p.id) == str(player1):
                player = p
            else:
                pass
        print('   > ' + player.fullname)

    @classmethod
    def new_tournament_page(cls, store):
        HomeView.chess_title()
        id_input = InputValidation.id_validation()
        name_input = InputValidation.name_validation()
        location_input = InputValidation.location_validation()
        date_input = InputValidation.date_validation()
        time_mode_input = InputValidation.time_mode_validation()
        description_input = InputValidation.description_validation()

        sp.call('clear', shell=True)
        HomeView.chess_title()
        PlayerView.player_list(store["players"])

        player1 = InputValidation.id_validation()
        TournamentView.print_name(store, player1)
        player2 = InputValidation.id_validation()
        TournamentView.print_name(store, player2)
        player3 = InputValidation.id_validation()
        TournamentView.print_name(store, player3)
        player4 = InputValidation.id_validation()
        TournamentView.print_name(store, player4)
        player5 = InputValidation.id_validation()
        TournamentView.print_name(store, player5)
        player6 = InputValidation.id_validation()
        TournamentView.print_name(store, player6)
        player7 = InputValidation.id_validation()
        TournamentView.print_name(store, player7)
        player8 = InputValidation.id_validation()
        TournamentView.print_name(store, player8)

        players_inputs = [player1,
                          player2,
                          player3,
                          player4,
                          player5,
                          player6,
                          player7,
                          player8]

        return {
            'tournament_id': id_input,
            'name': name_input.upper(),
            'location': location_input,
            'date': date_input,
            'time_mode': time_mode_input,
            'description': description_input,
            'player_ids': players_inputs,
        }

    @classmethod
    def tournament_list(cls, tournament):
        HomeView.chess_title()
        print('    ----------------------------------------------------------'
              '----------------------------')
        print("    [                                  TOURNAMENT LIST        "
              "                           ]")
        print('    ----------------------------------------------------------'
              '----------------------------')
        print("    [                                                         "
              "                           ]")
        print('    [  ID         Name,                 Location              '
              'Date            Time mode  ]')
        print("    [                                                         "
              "                           ]")
        for tournaments in tournament:
            print(f'    [  {tournaments.tournament_id}{space_id(tournaments)}'
                  f'       {tournaments.name},{space_name(tournaments)} '
                  f'{tournaments.location}{space_town(tournaments)}  '
                  f'{tournaments.date}          {tournaments.time_mode} '
                  '     ]')
        print("    [                                                         "
              "                           ]")
        print('    ----------------------------------------------------------'
              '----------------------------\n')
        print('    1. Start or Continue a Tournament            B. Back')
        print('    2. See Tournament details                    H. Homepage')
        print('    3. Delete Tournament                         Q. Exit\n')
        choice = input('    Choice: ')
        extra_info = None

        while True:
            try:
                if choice == '2':
                    extra_info = input(
                        'Enter Tournament Id to see Details (C. Cancel): '
                    )
                    if extra_info.lower() == 'c':
                        return 'tournaments_list', None
                    else:
                        return choice, int(extra_info)
                elif choice == '1':
                    extra_info = input(
                        'Enter Tournament Id to Start or Continue the Tournam'
                        'ent (C. Cancel): '
                    )
                    if extra_info.lower() == 'c':
                        return 'tournaments_list', None
                    else:
                        return choice, int(extra_info)
                elif choice == '3':
                    extra_info = input(
                        'Enter Tournament Id to delete it (C. Cancel): '
                    )
                    if extra_info.lower() == 'c':
                        return 'tournaments_list', None
                    else:
                        return choice, int(extra_info)
            except ValueError:
                print("invalid value")
            else:
                break
        return choice, extra_info

    @classmethod
    def tournament_details(cls, tournament):
        HomeView.chess_title()
        print('--------------------------------------------------------------'
              '--------------------------------')
        print("[                                   TOURNAMENT DESCRIPTION    "
              "                               ]")
        print('--------------------------------------------------------------'
              '--------------------------------\n')
        print(f'    ID : {tournament.tournament_id}')
        print(f'    Name : {tournament.name}')
        print(f'    Location : {tournament.location}')
        print(f'    Date : {tournament.date}')
        print(f'    Time Mode : {tournament.time_mode}')
        print(f'    Description : {tournament.description}\n')
        print('    Players :')
        PlayerView.player_list(tournament.players)
        print('    B. Back')
        print('    H. Homepage')
        print('    Q. Exit\n')

        choice = input('    Choice: ')
        if choice.lower() == 'b':
            return 'b'
        elif choice.lower() == 'h':
            return 'h'
        elif choice.lower() == 'q':
            return 'q'
        else:
            print("invalid ")
            return "tournament_detail", tournament.tournament_id

    @classmethod
    def start_tournament_page(cls, tournament):
        HomeView.chess_title()
        print('--------------------------------------------------------------'
              '--------------------------------')
        print("[                                   TOURNAMENT DESCRIPTION    "
              "                               ]")
        print('--------------------------------------------------------------'
              '--------------------------------\n')
        print(f'    ID : {tournament.tournament_id}')
        print(f'    Name : {tournament.name}')
        print(f'    Location : {tournament.location}')
        print(f'    Date : {tournament.date}')
        print(f'    Time Mode : {tournament.time_mode}')
        print(f'    Description : {tournament.description}\n')
        print('    Players :')
        print('    ---------------------------------------------------'
              '-----------------------------------')
        print('    [\tId\tName\t\t\t\t\t  Birth date\tSex\tRanking  ]')
        print('    ---------------------------------------------------'
              '-----------------------------------')

        for player in tournament.players:
            print(f'    [\t{player.id}\t{player.lastname} {player.firstname}'
                  f'{space(player)}           {player.birthdate}\t '
                  f'{player.sex}\t{player.ranking}\t ]        pts :   '
                  f'{tournament.scores[player.id]}')
        print('    ---------------------------------------------------'
              '-----------------------------------\n')

        print('')
        for round in tournament.rounds:
            print('----------------------------------------------------------'
                  '------------------------------------')
            print(f"[                                        "
                  f"{round.name.upper()}                                     "
                  "        ]")
            print('----------------------------------------------------------'
                  '------------------------------------')
            print('[  Game:  Player Id and Name:                VS           '
                  ' Player Id and Name:               ]')
            print('[                                                         '
                  '                                   ]')
            game_num = 0
            for game in round.games:
                game_num += 1
                print(f'[   ({game_num})   {game.player1.id} '
                      f'{game.player1.fullname} '
                      f'{win(game.winner, game.player1)}{space(game.player1)}'
                      f'vs          {win(game.winner, game.player2)}'
                      f' {game.player2.id} {game.player2.fullname}'
                      f'{space(game.player2)} ]')
            print('----------------------------------------------------------'
                  '------------------------------------\n')
            print('\n')
        if tournament.finished_tournament():
            print('\n--------------------------------------------------------'
                  '--------------------------------------')
            print("[                                   TOURNAMENT RESULTS    "
                  "                                   ]")
            print('----------------------------------------------------------'
                  '------------------------------------\n')
            for player in tournament.players:
                print(f'                {player.fullname} :{space(player)}'
                      f'{tournament.scores[player.id]}')
        else:
            print('1. Game (1)')
            if tournament.rounds[-1].games[0].winner is not None:
                if not tournament.rounds[-1].games[0].winner:
                    print('Draw')
                else:
                    print(f'    Winner : '
                          f'{tournament.rounds[-1].games[0].winner.fullname}')

            print('2. Game (2)')
            if tournament.rounds[-1].games[1].winner is not None:
                if not tournament.rounds[-1].games[1].winner:
                    print('Draw')
                else:
                    print(f'    Winner : '
                          f'{tournament.rounds[-1].games[1].winner.fullname}')

            print('3. Game (3)')
            if tournament.rounds[-1].games[2].winner is not None:
                if not tournament.rounds[-1].games[2].winner:
                    print('Draw')
                else:
                    print(f'    Winner : '
                          f'{tournament.rounds[-1].games[2].winner.fullname}')

            print('4. Game (4)')
            if tournament.rounds[-1].games[3].winner is not None:
                if not tournament.rounds[-1].games[3].winner:
                    print('Draw')
                else:
                    print(f'    Winner : '
                          f'{tournament.rounds[-1].games[3].winner.fullname}')

        print('\n\nB. Back')
        print('H. Homepage                              A. Show players by al'
              'phabetical order')
        print('Q. Exit                                  R. Show players by ra'
              'nking\n')

        choice = input('Choice: ')
        if choice in "1234":
            choice = int(choice)
        else:
            if choice.lower() == 'b':
                return 'b', None
            elif choice.lower() == 'h':
                return 'h', None
            elif choice.lower() == 'q':
                return 'q', None
            elif choice.lower() == 'a':
                return 'alpha', None
            elif choice.lower() == 'r':
                return 'rank', None
            else:
                print("invalid value ")
                return "tournament_start", tournament.tournament_id

        while True:
            try:
                extra_info = input(
                    f'1. {round.games[choice -1].player1.fullname}\n'
                    f'2. {round.games[choice -1].player2.fullname}\n'
                    '3. draw\n'
                    'Enter winner  ("C" to cancel): '
                    )
                if extra_info == 'c':
                    return 'tournament_start', None
                elif extra_info in '123':
                    return choice, int(extra_info)
                else:
                    print("invalid value ")
                return choice, int(extra_info)
            except ValueError:
                print("invalid value")
            else:
                break
            return choice, extra_info
