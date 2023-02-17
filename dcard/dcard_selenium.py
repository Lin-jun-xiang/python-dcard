from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
import time
import chromedriver_autoinstaller
from .decorate import timeit

class Api:
    """The selenium selectors : https://selenium-python.readthedocs.io/locating-elements.html"""

    HOST = "https://www.dcard.tw/"

    def __init__(self):
        chromedriver_autoinstaller.install(path="./driver/")  # Check if the current version of chromedriver exists
                                                            # and if it doesn't exist, download it automatically,
                                                            # then add chromedriver to path
                                                            # "C://Program File(x86)/Google/Chrome" should be exists
        # If cannot find then specific the driver path
        self.driver = webdriver.Chrome("./driver/chromedriver_win32/chromedriver.exe")

    @timeit
    def get_popular_forums(self) -> list:
        """熱門看板"""
        self.driver.get(Api.HOST + "forum/popular")

        self.driver.maximize_window()

        scroll_to_bottom(self.driver)

        # Check the max numbers of popular forums
        forum_tag = self.driver.find_element(By.XPATH,
                                         '//*[@id="__next"]/div[2]/div[2]/div/div/div/div/div')
        forum_list_nums = len(forum_tag.find_elements(By.TAG_NAME,
                                                    "a"))

        i = 1
        popular_forums = []
        while i < number_limit or i > forum_list_nums:
            try:
                forum = self.driver.find_element(By.XPATH,
                                            f'//*[@id="__next"]/div[2]/div[2]/div/div/div/div/div/a[{i}]/div/div[3]')
                popular_forums.append(forum.text)
                print(f"Popular forum-{i}")

            except Exception as e:
                logging.error('Error at %s', 'No more forums', exc_info=e)
                break

            i += 1

        return popular_forums

    @timeit
    def get_sensity_forums(self):
        """精選看板"""
        self.driver.get(Api.HOST + "forum/popular")

        self.driver.maximize_window()
        scroll_to_bottom(self.driver)

        forum_tag = self.driver.find_element(By.XPATH,
                                         '//*[@id="__next"]/div[2]/div[1]/div/div')
        forum_list_nums = len(forum_tag.find_elements(By.TAG_NAME,
                                                    "a"))

        i = 1
        sensity_forums = []
        while i < number_limit or i > forum_list_nums:
            try:
                forum = self.driver.find_element(By.XPATH,
                                            f'//*[@id="__next"]/div[2]/div[1]/div/div/a[{i}]/div/div[2]')
                sensity_forums.append(forum.text)
                print(f"Sensity forum-{i}")

            except Exception as e:
                logging.warning('Error at %s', 'No more forums', exc_info=e)
                break

            i += 1

        return sensity_forums

    def close(self):
        self.driver.close()

def scroll_to_bottom(driver):
    SCROLL_PAUSE_TIME = 0.9

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
