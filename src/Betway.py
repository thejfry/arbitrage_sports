from Webscraper import Bookkeeper


class SportsInteraction(Bookkeeper):

    def __init__(self):
        super.__init__()
        self.home = 'https://sports.betway.com/en/sports'

    def open_home(self):
        self.driver.get(self.home)

    def get_odds(self):
        pass