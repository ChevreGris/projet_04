import subprocess as sp
from exceptions import InputException
from views.player_view import PlayerView

class Tournament:

    def __init__(self, tournament_id, name, location, date,
                 time_mode, description, players) -> None:
        self.tournament_id = tournament_id
        self.name = name
        self.location = location
        self.date = date
        self.rounds = []
        self.time_mode = time_mode
        self.description = description
        self.players = players

    @classmethod
    def TournamentValidation(cls, store, route_params=None):

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
            name_input = input("Enter Tournament's name: ")
            try:
                if not name_input.isalpha():
                    raise InputException(
                        'invalid name, must only contain letters.'
                    )

                elif len(name_input) > 20:
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
        
        sp.call('clear', shell=True)
        PlayerView.player_list(store["players"])

        player1 = input('Player 1 ID: ')
        player2 = input('Player 2 ID: ')
        player3 = input('Player 3 ID: ')
        player4 = input('Player 4 ID: ')
        player5 = input('Player 5 ID: ')
        player6 = input('Player 6 ID: ')
        player7 = input('Player 7 ID: ')
        player8 = input('Player 8 ID: ')

        players_inputs = [player1, player2, player3, player4, player5, player6, player7, player8]

        return {

            'tournament_id': id_input,
            'name': name_input.upper(),
            'location': location_input.capitalize(),
            'date': date_input,
            'time_mode': time_mode_input,
            'description': description_input,
            'players': players_inputs
        }