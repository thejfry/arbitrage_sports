from selenium import webdriver


class Webscraper:

    def __init__(self):
        self.driver = webdriver.Chrome("C:\Program Files\chromedriver_win32\chromedriver.exe")
