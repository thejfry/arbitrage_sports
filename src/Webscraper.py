from selenium import webdriver
from abc import abstractmethod
import numpy as np
import pandas as pd

class Webscraper:

    def __init__(self):
        self.driver = webdriver.Chrome("C:\Program Files\chromedriver_win32\chromedriver.exe")
        self.games_df = pd.DataFrame()

    def print_games(self):
        print(self.games_df)

    def close_browser(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()


class Bookkeeper(Webscraper):

    def __init__(self):
        super.__init__()

    @abstractmethod
    def open_home(self):
        pass

    @abstractmethod
    def get_leagues(self):
        pass
    
    @abstractmethod
    def get_odds(self):
        pass