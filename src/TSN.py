from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
import asyncio

import time
from datetime import datetime
from dateutil.parser import parse

import numpy as np
import pandas as pd

from Webscraper import Webscraper

# class TSN_bs4:
#
#     def __init__(self):
#         self.home_url = 'https://www.tsn.ca/'
#
#     def open_home(self):
#         # TODO: figure out what to do with this soup, or delete this method
#         home_soup = requests.get(self.home_url)
#
#     def get_games(self, league, date=None):
#         page_soup = get_soup(self.home_url + '/' + league.lower() + '/schedule')
#
#         # check that date is correct
#         page_date = page_soup.find_all('widgets-bms-schedule')
#
#         # loop through games making list of objects
#
#
#         # print(page_soup.prettify)
#         print(page_date)
#
# def get_soup(url):
#     temp_page = requests.get(url)
#     return BeautifulSoup(temp_page.content, 'html.parser')

class TSN_selenium(Webscraper):

    def __init__(self):
        super().__init__()
        self.home = 'https://www.tsn.ca/'
        self.games = {'team_home': [], 'team_away': [], 'startTime': []}

    def open_home(self):
        self.driver.get(self.home)

    def get_games(self, league, date=None):
        # navigate to schedule webpage
        self.driver.get(self.home + '/' + league.lower() + '/schedule')
        time.sleep(5)

        # find and expand shadow root
        shadow_section_element = self.driver.find_element_by_css_selector('widgets-bms-schedule')
        shadow_section = expand_shadow_element(self.driver, shadow_section_element)

        # isolate today's games
        today_elem = shadow_section.find_element_by_css_selector('.bms-schedule-details__day')

        # get date from the schedule
        dateText = today_elem.find_element_by_css_selector('.bms-schedule-details__day-header').text

        # get team1, team2, and startTime from all games on the given date
        game_elements = today_elem.find_elements_by_css_selector('.bms-schedule-details__event')
        for game in game_elements:
            startTime = game.find_element_by_css_selector('.bms-schedule-details__event-status').text.strip()
            self.games['startTime'].append(' '.join([dateText, startTime]))
            # TODO: convert date to datetime object
            # games[startTime] = datetime.strptime(startTime, '%A %b %d')

            self.games['team_home'].append(game.find_element_by_css_selector(
                '.bms-schedule-details__event-team--home').find_element_by_css_selector(
                '.bms-schedule-details__team-name').text.strip())
            self.games['team_away'].append(game.find_element_by_css_selector(
                '.bms-schedule-details__event-team--away').find_element_by_css_selector(
                '.bms-schedule-details__team-name').text.strip())

        # convert dictionary to dataframe for adding betting odds
        self.games_df = pd.DataFrame.from_dict(self.games)
        self.print_games()

    def close_browser(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()


def expand_shadow_element(driver_, element):
    driver = driver_
    return driver.execute_script('return arguments[0].shadowRoot', element)

