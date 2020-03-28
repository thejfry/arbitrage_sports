'''
This will be a webscraper that keeps track of all sporting events on each day.

Author: Jeffrey Plett
Date: March 23, 2020
'''

import time

from TSN import TSN_selenium

def data_collection():
    tsn_se = TSN_selenium()
    tsn_se.get_games('mlb')
    tsn_se.get_games('nhl')

    tsn_se.quit()

if __name__ == "__main__":
    print('start')
    data_collection()
    print('end')
