from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
import time
class Api:
    """The selenium selectors : https://selenium-python.readthedocs.io/locating-elements.html"""

    host = "https://www.dcard.tw/"

    def __init__(self):
        self.chromePath = "./driver/chromedriver_win32/chromedriver.exe"
        self.driver = webdriver.Chrome(self.chromePath)

    def get_popular_forums(self, number_limit : int=400):
        self.driver.get(Api.host + "forum/popular")

        self.driver.maximize_window()

        # scroll to bottom of page
        scroll_to_bottom(self.driver)
        

        # check the max numbers of popular forums
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
                print(f"...{i}")

            except Exception as e:
                logging.error('Error at %s', 'No more forums', exc_info=e)
                break

            i += 1

        self.driver.close()

        return popular_forums

def scroll_to_bottom(driver):
    SCROLL_PAUSE_TIME = 0.7

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
