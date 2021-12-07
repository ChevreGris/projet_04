class HomeView:

    @classmethod
    def home(cls):
        print("\n")
        print("                      .d8888b.  888                                   888")
        print("                     d88P  Y88b 888                                   888")
        print("                     888    888 888                                   888")
        print("                     888        88888b.   .d88b.  .d8888b  .d8888b    888")
        print('                     888        888 "88b d8P  Y8b 88K      88K        Y8P')
        print('                     888    888 888  888 88888888 "Y8888b. "Y8888b.      ')
        print("                     Y88b  d88P 888  888 Y8b.          X88      X88   d8b")
        print("                      'Y8888P'  888  888  'Y8888   88888P'  88888P'   Y8P")
        print("")
        print("----------------------------------------------------------------------------------------------")
        print(" A chess tournament manager                                                          v0.08.00")
        print("----------------------------------------------------------------------------------------------\n")
        print("1. Players")
        print("2. Tournaments\n")
        print("Q. Exit\n")

        return input("Choice: ")
        