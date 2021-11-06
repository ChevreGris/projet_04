from models.player import Player
from views.player_view import PlayerView
from exceptions import InputException


class PlayerController:

    @classmethod
    def home_list(cls, store, route_params=None):
        choice, player_id = PlayerView.home_player_list(store["players"])

        if choice == "1":
            return "new_player", None
        elif choice == "2":
            return "edit_player", player_id
        elif choice == "3":
            return "delete_player", player_id
        elif choice == "q":
            return "quit", None
        elif choice.lower() == "h":
            return "homepage", None
        else:
            print("invalid value ")
            return "home_player", None

    @classmethod
    def create(cls, store, route_params=None):
        data = PlayerView.create_player()
        player = Player(**data)
        store["players"].append(player)
        return "home_player", None

    @classmethod
    def delete(cls, store, route_params):
        store["players"] = [
            p for p in store["players"] if p.id != route_params
        ]
        return "home_player", None

    @classmethod
    def edit(cls, store, route_params):
        
        player = next(p for p in store["players"] if p.id == route_params)
        
        choice = PlayerView.edit_player(player)
        
        if choice.lower() == "1":
            while True:
                id_input = input('Enter new ID: ')
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
            return{'id': id_input}

        elif choice.lower() == "2":
            while True:
                lastname_input = input('Enter new lastname: ')
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
            return{'lastname': lastname_input.upper()}

        elif choice.lower() == "3":
            while True:
                firstname_input = input('Enter new firstname: ')
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
            return{'firstname': firstname_input.capitalize()}

        elif choice.lower() == "4":
            while True:
                birthdate_input = input('Enter new birthdate (DD/MM/YYYY): ')
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
            return{'birthdate': birthdate_input}

        elif choice.lower() == "5":
            while True:
                sex_input = input('Enter new sex (F or M): ')
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
            return{'sex': sex_input.upper()}

        elif choice.lower() == "6":
            while True:
                ranking_input = input('Enter new ranking: ')
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
            return{'ranking': ranking_input}

        elif choice.lower() == "b":
            return "home_player", None
        elif choice.lower() == "h":
            return "homepage", None
        elif choice.lower() == "q":
            return "quit", None
        else:
            print("invalid value")
            return "edit_player", None
