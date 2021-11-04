class HomeView:

    @classmethod
    def home(cls):
        print("Welcome\n")
        print("1. Players")
        print("2. Tournaments\n")
        print("Q. Exit")

        return input("Choice: ")
