from selenium import webdriver
from selenium.webdriver.common.by import By
import time

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

            except Exception as e:
                print("Crawler finished! No more forum")
                break
            
            i += 1

        return popular_forums


api = Api()

