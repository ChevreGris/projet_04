from exceptions import InputException


class Player:
    def __init__(self, id, lastname, firstname, birthdate, sex, ranking) -> None:
        self.id = id
        self.lastname = lastname
        self.firstname = firstname
        self.birthdate = birthdate
        self.sex = sex
        self.ranking = ranking

    @classmethod
    def Validation(cls):
        while True:
            id_input = input('Enter an ID: ')
            try:
                int(id_input)
                if int(id_input) > 9999:
                    raise InputException('invalid ID, max ID is 9999.')
            except InputException as e:
                print(f'error : {str(e)}')
            except ValueError:
                print('error, must be a number.')
            else:
                break

        while True:
            lastname_input = input('Enter your lastname: ')
            try:
                if not lastname_input.isalpha():
                    raise InputException(
                        'invalid lastname, must only contain letters.'
                    )

                elif len(lastname_input) > 20:
                    raise InputException(
                        'Lastname too long (max 20 caracter).'
                    )
                elif len(lastname_input) < 3:
                    raise InputException(
                        'Lastname too short (min 3 caracter).'
                    )
            except InputException as e:
                print(f'error : {str(e)}')
            else:
                break

        while True:
            firstname_input = input('Enter your firstname: ')
            try:
                if not firstname_input.isalpha():
                    raise InputException(
                        'invalid firstname, must only contain letters.'
                    )
                elif len(firstname_input) > 20:
                    raise InputException(
                        'Firstname too long (max 20 caracter).'
                    )
                elif len(firstname_input) < 3:
                    raise InputException(
                        'Firstname too short (min 3 caracter).'
                    )
            except InputException as e:
                print(f'error : {str(e)}')
            else:
                break

        while True:
            birthdate_input = input('Enter birthdate (DD/MM/YYYY): ')
            try:
                if len(birthdate_input) > 10:
                    raise InputException(
                        'Birthday incorect (must be : DD/MM/YYYY).'
                    )
                elif len(birthdate_input) < 10:
                    raise InputException(
                        'Birthday incorect (must be : DD/MM/YYYY).'
                        )
                elif '/' not in birthdate_input:
                    raise InputException(
                        'Birthday incorect (must be : DD/MM/YYYY).'
                        )
                elif '19' not in birthdate_input:
                    if '20' not in birthdate_input:
                        raise InputException(
                            'Birthday incorect (year must be in 1900 OR 2000).'
                        )
            except InputException as e:
                print(f'error : {str(e)}')
            else:
                break

        while True:
            sex_input = input('Enter your sex (F or M): ')
            try:
                if sex_input == 'M':
                    break
                elif sex_input == 'F':
                    break
                elif sex_input == 'm':
                    break
                elif sex_input == 'f':
                    break
                else:
                    raise InputException('Sex invalid (must be "M" or "F").')
            except InputException as e:
                print(f'error : {str(e)}')
            else:
                break

        while True:
            ranking_input = input('Enter ranking: ')
            try:
                int(ranking_input)
                if int(ranking_input) > 2882:
                    raise InputException(
                        'Ranking too big (max ranking : 2882 )'
                    )
                elif int(ranking_input) < 1:
                    raise InputException(
                        'Lastname too small (min ranking : 1)'
                    )
            except InputException as e:
                print(f'error : {str(e)}')
            except ValueError:
                print('error, must be a number.')
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