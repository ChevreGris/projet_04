from os import error


class PlayerView:

    @classmethod
    def display_list(cls, players):
        print('    ---------------------------------------------------'
              '---------------------------')
        print('    [\tId\tName\t\t\t\tBirth date\tSex\tRanking  ]')
        print('    ---------------------------------------------------'
              '---------------------------')
        for player in players:
            print(f'    [\t{player.id}\t{player.lastname} {player.firstname}'
                  f'\t\t\t{player.birthdate}\t{player.sex}\t{player.ranking}'
                  f'\t ]')
        print('    ---------------------------------------------------'
              '---------------------------')
        print('')
        print('1. View Player')
        print('2. New Player                H. Homepage')
        print('3. Delete Player             Q. Exit')

        choice = input('Choice:')
        extra_info = None

        if choice in ('1', '3'):
            extra_info = int(input('Enter Player Id:'))
        return choice, extra_info

    @classmethod
    def detail_player(cls, player):
        print('     Player info :')
        print('    ---------------------------------------------------'
              '---------------------------')
        print('    [\tId\tName\t\t\t\tBirth date\tSex\tRanking  ]')
        print('    ---------------------------------------------------'
              '---------------------------')
        print(f'    [\t{player.id}\t{player.lastname} {player.firstname}'
              f'\t\t\t{player.birthdate}\t{player.sex}\t{player.ranking}'
              f'\t ]')
        print('    ---------------------------------------------------'
              '---------------------------')
        print('')
        print('1. Edit info')
        print('')
        print('Q. Exit')
        print('H. Homepage')
        return input('Choice:')

    @classmethod
    def create_player(cls):
        while True:
            id_input = input('Enter an ID: ')
            try:
                int(id_input)
                if len(id_input) < 1:
                    error_id = int('id_too_short')
            except ValueError:
                print('\n"' + id_input + '" is not a valid number,'
                      ' try again.')
            else:
                break

        while True:
            lastname_input = input('Enter your lastname: ')
            try:
                if len(lastname_input) > 20:
                    error_name = int('name_too_long')
                elif len(lastname_input) < 3:
                    error_name = int('name_too_short')
            except ValueError:
                print('Lastname too long (max 20 caracter) or '
                      'to short (min 3 caracter), please try again.')
            else:
                break

        while True:
            firstname_input = input('Enter your firstname: ')
            try:
                if len(firstname_input) > 20:
                    error_name = int('name_too_long')
                elif len(firstname_input) < 3:
                    error_name = int('name_too_short')
            except ValueError:
                print('Firstname too long (max 20 caracter) '
                      'or to short (min 3 caracter), please try again.')
            else:
                break

        while True:
            birthdate_input = input('Enter birthdate (DD/MM/YYYY): ')
            try:
                if len(birthdate_input) > 10:
                    error_age = int('age_too_long')
                elif len(birthdate_input) < 10:
                    error_age = int('age_too_short')
                elif '/' not in birthdate_input:
                    error_age = int('age_no_slash')
            except ValueError:
                print('\n"' + birthdate_input + '" is not a valid '
                      'birthdate, try again.')
            else:
                break

        while True:
            sex_input = input('Enter your sex (F or M): ')
            try:
                if sex_input == 'M':
                    break
                elif sex_input == 'F':
                    break
                else:
                    error_sex = int('sex_incorect')
            except ValueError:
                print('\n"' + sex_input + '" is not a valid sex, try again.')
            else:
                break

        while True:
            ranking_input = input('Enter ranking: ')
            try:
                if int(ranking_input) > 9999:
                    error_age = int('age_too_long')
                elif int(ranking_input) < 1:
                    error_age = int('age_too_short')
            except ValueError:
                print('\n"' + ranking_input + '" is not a valid ranking,'
                      ' try again.')
            else:
                break

        return {

            'id': id_input,
            'lastname': lastname_input.upper(),
            'firstname': firstname_input.capitalize(),
            'birthdate': birthdate_input,
            'sex': sex_input.upper(),
            'ranking': ranking_input
        }

    @classmethod
    def edit_player(cls):
        print('fonction en cours de creation !')
        print('Q. Exit')
        print('H. Homepage')
        return input('Choice:')
