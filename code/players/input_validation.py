from exceptions import InputException


class InputValidation():
    
    @classmethod
    def id_validation(self):
        #Error management and input validation for the ID input
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

        return id_input

    @classmethod
    def name_validation(self):
        #Error management and input validation for the Name input
        while True:
            name_input = input("Enter Tournament's name: ")
            try:
                if len(name_input) > 20:
                    raise InputException(
                        'name too long (max 20 caracter).'
                    )
                elif len(name_input) < 3:
                    raise InputException(
                        'name too short (min 3 caracter).'
                    )
            except InputException as e:
                print(f'error : {str(e)}')
            else:
                break

        return name_input

    @classmethod
    def location_validation(self):
        #Error management and input validation for the Location input
        while True:
            location_input = input('Enter Tournament location: ')
            try:
                if not location_input.isalpha():
                    raise InputException(
                        'invalid location, must only contain letters.'
                    )
                elif len(location_input) > 20:
                    raise InputException(
                        'location too long (max 20 caracter).'
                    )
                elif len(location_input) < 3:
                    raise InputException(
                        'location too short (min 3 caracter).'
                    )
            except InputException as e:
                print(f'error : {str(e)}')
            else:
                break

    @classmethod
    def date_validation(self):
        #Error management and input validation for the Date input
        while True:
            date_input = input('Enter date (DD/MM/YYYY): ')
            try:
                if len(date_input) > 10:
                    raise InputException(
                        'date incorect (must be : DD/MM/YYYY).'
                    )
                elif len(date_input) < 10:
                    raise InputException(
                        'date incorect (must be : DD/MM/YYYY).'
                        )
                elif '/' not in date_input:
                    raise InputException(
                        'date incorect (must be : DD/MM/YYYY).'
                        )
                elif '20' not in date_input:
                    raise InputException(
                        'date incorect (year must be in 2000).'
                    )
            except InputException as e:
                print(f'error : {str(e)}')
            else:
                break

        return date_input

    @classmethod
    def time_mode_validation(self):
        #Error management and input validation for the Time mode input
        while True:
            time_mode_input = input('Enter time mode (A : Bullet, B : Blitz or C : Quick_it):')
            try:
                if time_mode_input == 'A':
                    break
                elif time_mode_input == 'B':
                    break
                elif time_mode_input == 'C':
                    break
                elif time_mode_input == 'a':
                    break
                elif time_mode_input == 'b':
                    break
                elif time_mode_input == 'c':
                    break
                else:
                    raise InputException('invalid time mode(must be "A", "B" or "C").')
            except InputException as e:
                    print(f'error : {str(e)}')
            else:
                break

        return time_mode_input
            
    @classmethod
    def description_validation(self):
        #Error management and input validation for the description input
        while True:
            description_input = input('Enter description of the tournament:')
            try:
                if len(description_input) > 99:
                    raise InputException('description too long, max 99 caracter.')
                elif len(description_input) < 3:
                    raise InputException('description too short, min 3 caracter.')
            except InputException as e:
                print(f'error : {str(e)}')
            else:
                break

        return description_input

    @classmethod
    def lastname_validation(self):
        #Error management and input validation for the Lastname input
        while True:
            lastname_input = input('Enter your lastname: ')
            try:
                if not lastname_input.isalpha():
                    raise InputException(
                        'invalid lastname, must only contain letters.'
                    )

                elif len(lastname_input) > 15:
                    raise InputException(
                        'Lastname too long (max 15 caracter).'
                    )
                elif len(lastname_input) < 3:
                    raise InputException(
                        'Lastname too short (min 3 caracter).'
                    )
            except InputException as e:
                print(f'error : {str(e)}')
            else:
                break

        return lastname_input

    @classmethod
    def firstname_validation(self):
        #Error management and input validation for the Firstname input
        while True:
            firstname_input = input('Enter your firstname: ')
            try:
                if not firstname_input.isalpha():
                    raise InputException(
                        'invalid firstname, must only contain letters.'
                    )
                elif len(firstname_input) > 15:
                    raise InputException(
                        'Firstname too long (max 15 caracter).'
                    )
                elif len(firstname_input) < 3:
                    raise InputException(
                        'Firstname too short (min 3 caracter).'
                    )
            except InputException as e:
                print(f'error : {str(e)}')
            else:
                break
        
        return firstname_input

    @classmethod
    def birthdate_validation(self):
        #Error management and input validation for the Birthdate input
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

        return birthdate_input

    @classmethod
    def sex_validation(self):
        #Error management and input validation for the Sex input
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

        return sex_input

    @classmethod
    def ranking_validation(self):
        #Error management and input validation for the Ranking input
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

        return ranking_input

    @classmethod
    def lenght_to_max(self, lname, fname):
        #set the space betwin name and date in player menu
        if len(fname + lname) == 6:
            max_lenght = '                        '
        elif len(fname + lname) == 7:
            max_lenght = '                       '
        elif len(fname + lname) == 8:
            max_lenght = '                      '
        elif len(fname + lname) == 9:
            max_lenght = '                     '
        elif len(fname + lname) == 10:
            max_lenght = '                    '
        elif len(fname + lname) == 11:
            max_lenght = '                   '
        elif len(fname + lname) == 12:
            max_lenght = '                  '
        elif len(fname + lname) == 13:
            max_lenght = '                 '
        elif len(fname + lname) == 14:
            max_lenght = '                '
        elif len(fname + lname) == 15:
            max_lenght = '               '
        elif len(fname + lname) == 16:
            max_lenght = '              '
        elif len(fname + lname) == 17:
            max_lenght = '             '
        elif len(fname + lname) == 18:
            max_lenght = '            '
        elif len(fname + lname) == 19:
            max_lenght = '           '
        elif len(fname + lname) == 20:
            max_lenght = '          '
        elif len(fname + lname) == 21:
            max_lenght = '         '
        elif len(fname + lname) == 22:
            max_lenght = '        '
        elif len(fname + lname) == 23:
            max_lenght = '       '
        elif len(fname + lname) == 24:
            max_lenght = '      '
        elif len(fname + lname) == 25:
            max_lenght = '     '
        elif len(fname + lname) == 26:
            max_lenght = '    '
        elif len(fname + lname) == 27:
            max_lenght = '   '
        elif len(fname + lname) == 28:
            max_lenght = '  '
        elif len(fname + lname) == 29:
            max_lenght = ' '
        elif len(fname + lname) == 30:
            max_lenght = ''
        
        return max_lenght
