from views.home_view import HomeView


class HomePageController:

    @classmethod
    def dispatch(cls, store=None, input=None):
        choice = HomeView.home()
        if choice.lower() == "1":
            next = "home_player"
        elif choice == "2":
            next = "home_tournament"
        elif choice == "q":
            next = "quit"
        else:
            next = "homepage"
            print("invalid value")
        return next, None
