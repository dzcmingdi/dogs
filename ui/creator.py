import ui.home as home

class Creator:
    def __init__(self,window):
        self.window = window
        self.home_init = home.HomeInit(window)

    def create(self):
        self.home_init.init_view()

