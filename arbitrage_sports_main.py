'''
This will be a webscraper that keeps track of all sporting events on each day.

Author: Jeffrey Plett
Date: March 23, 2020
'''

import time

from TSN import TSN_selenium

# TODO: Make 'API' for each site so I can call something like TSN.baseball.get_games()
if __name__ == "__main__":
    print('start')
    # tsn_bs4 = TSN_bs4()
    # tsn_bs4.open_home()
    # tsn_bs4.get_games('mlb')

    tsn_se = TSN_selenium()
    # tsn_se.open_home()
    tsn_se.get_games('mlb')
    
    time.sleep(10)
    tsn_se.quit()
    print('end')
