from selenium import webdriver
from selenium.webdriver.common.by import By
import logging

class Api:

    host = "https://www.dcard.tw/"

    def __init__(self):
        self.chromePath = "./driver/chromedriver_win32/chromedriver.exe"
        self.driver = webdriver.Chrome(self.chromePath)

    def get_popular_forums(self):
        self.driver.get(Api.host + "forum/popular")

        self.driver.maximize_window()

        i = 1
        popular_forums = []
        while True:
            try:
                forum = self.driver.find_element(By.XPATH,
                                            f'//*[@id="__next"]/div[2]/div[2]/div/div/div/div/div/a[{i}]/div/div[3]')
                popular_forums.append(forum.text)
                print(f"...{i}")

            except Exception as e:
                logging.error('Error at %s', 'No more forums', exc_info=e)
                break

            i += 1

        self.driver.close()

        return popular_forums
