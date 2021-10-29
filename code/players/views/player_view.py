from os import error


class PlayerView:

    @classmethod
    def display_list(cls, players):
        print("\tID\tName\tAge")
        for player in players:
            print(f"\t{player.id}\t{player.name}\t{player.age}")

        print("1. View Player")
        print("2. New Player")
        print("3. Delete Player")
        print("Q. Exit")
        print("H. Homepage")

        choice = input("Choice:")
        extra_info = None

        if choice in ("1", "3"):
            extra_info = int(input("Enter Player Id:"))

        return choice, extra_info

    @classmethod
    def detail_player(cls, player):
        print(f"Id: {player.id}")
        print(f"Name: {player.name}")
        print(f"Age: {player.age}")
        print(f"Email: {player.email}")

        print("Q. Exit")
        print("H. Homepage")
        return input("Choice:")

    @classmethod
    def create_player(cls):
        while True:
            id_input = input("Enter an ID: ")
            try:
                int(id_input)
                if len(id_input) < 1:
                    error_id = int("id_too_short")
            except ValueError:
                print('\n"' + id_input + '" is not a valid number, try again.')
            else:
                break

        while True:
            name_input = input("Enter a name: ")
            try:
                if len(name_input) > 20:
                    error_name = int("name_too_long")
                elif len(name_input) < 3:
                    error_name = int("name_too_short")
            except ValueError:
                print('Name too long (max 20 caracter) or incorect caracter, please try again.')
            else:
                break

        while True:
            age_input = input("Enter an age: ")
            try:
                if int(age_input) > 150:
                    error_age = int("age_too_long")
            except ValueError:
                print('\n"' + age_input + '" is not a valid number (max 150), try again.')
            else:
                break

        while True:
            email_input = input("Enter an email: ")
            try:
                if "@" and "." not in email_input :
                    error_email = int("invalide_email")
                elif len(email_input) > 100:
                    error_email = int("email_too_long")
            except ValueError:
                print('\n"' + email_input + '" is not a valid email, try again.')
            else:
                break
        
        return {
            
            "id": id_input,
            "name": name_input,
            "age": age_input,
            "email": email_input
        }
