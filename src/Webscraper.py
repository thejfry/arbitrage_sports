from selenium import webdriver
import numpy as np
import pandas as pd

class Webscraper:

    def __init__(self):
        self.driver = webdriver.Chrome("C:\Program Files\chromedriver_win32\chromedriver.exe")
        self.games_df = pd.DataFrame()

    def print_games(self):
        print(self.games_df)