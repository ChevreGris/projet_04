import subprocess as sp
from input_validation import InputValidation

def space(player):
    #set the space betwin name and date in player menu
    max_lenght = 30 - len(player.lastname + player.firstname)
    return " " * max_lenght

class PlayerView:
    @classmethod
    def player_list(cls, players):
        print('    ---------------------------------------------------'
              '-----------------------------------')
        print('    [\tId\tName\t\t\t\t\t  Birth date\tSex\tRanking  ]')
        print('    ---------------------------------------------------'
              '-----------------------------------')

        for player in players:
            print(f'    [\t{player.id}\t{player.lastname} {player.firstname}{space(player)}'
                  f'           {player.birthdate}\t {player.sex}\t{player.ranking}'
                  f'\t ]')
        print('    ---------------------------------------------------'
              '-----------------------------------\n')

    @classmethod
    def home_player_list(cls, players):
        print('    ---------------------------------------------------'
              '-----------------------------------')
        print('    [\tId\tName\t\t\t\t\t  Birth date\tSex\tRanking  ]')
        print('    ---------------------------------------------------'
              '-----------------------------------')
        for player in players:
            print(f'    [\t{player.id}\t{player.lastname} {player.firstname}{space(player)}'
                  f'           {player.birthdate}\t {player.sex}\t{player.ranking}'
                  f'\t ]')
        print('    ---------------------------------------------------'
              '-----------------------------------\n')
        print('    1. New player')
        print('    2. Edit Player               H. Homepage')
        print('    3. Delete Player             Q. Exit')
        print('')

        choice = input('    Choice: ')
        extra_info = None

        while True:
            try:
                if choice == '2':
                    sp.call('clear', shell=True)
                    PlayerView.player_list(players)
                    extra_info = input(
                        '\nTo edit Player info : \n\nEnter Player Id (C. Cancel): '
                    )
                    if extra_info.lower() == 'c':
                        return 'home_player', None
                    else:
                        return choice, int(extra_info)
                elif choice == '3':
                    sp.call('clear', shell=True)
                    PlayerView.player_list(players)
                    extra_info = input(
                        '\nTo delete Player:\n\nEnter Player Id (C. Cancel): '
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
    def create_player(cls):
        id_input = InputValidation.id_validation()
        lastname_input = InputValidation.lastname_validation()
        firstname_input = InputValidation.firstname_validation()
        birthdate_input = InputValidation.birthdate_validation()
        sex_input = InputValidation.sex_validation()
        ranking_input = InputValidation.ranking_validation()

        return {
            'id': id_input,
            'lastname': lastname_input.upper(),
            'firstname': firstname_input.capitalize(),
            'birthdate': birthdate_input,
            'sex': sex_input.upper(),
            'ranking': ranking_input
        }

    @classmethod
    def edit_player(cls, player):
        sp.call('clear', shell=True)
        print('Edit :\n')
        print(f'     1. ID :            {player.id}')
        print(f'     2. lastname :      {player.lastname}')
        print(f'     3. firstname :     {player.firstname}')
        print(f'     4. birthdate :     {player.birthdate}             '
              '              B. Back')
        print(f'     5. sex :           {player.sex}                   '
              '                 Q. Exit')
        print(f'     6. ranking :       {player.ranking}               '
              '                  H. Homepage\n\n')

        choice = input('Choice: ')
        return choice


