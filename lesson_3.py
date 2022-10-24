from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from auth_date import username, password
import time
import random


class InstagramBot():

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self,browser = webdriver.Chrome(r'C:\Python\Instagram_Bot\chromedriver\chromedriver')

    def close_browser(self):
        self.browser.close()
        self.browser.quit()

    def ligin(self):

        browser = self.browser
        browser.get('https://www.instagram.com')
        time.sleep(random.randrange(1, 3))

        username_input = browser.find_element(By.NAME, 'username')
        username_input.clear()
        username_input.send_keys(username)

        time.sleep(2)

        password_input = browser.find_element(By.NAME, 'password')
        password_input.clear()
        password_input.send_keys(password)

        password_input.send_keys(Keys.ENTER)
        time.sleep(20)

    def like_foto_by_hashtag(self, hashtag):
        browser = self.browser
        try:
            browser.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
            time.sleep(10)

            for i in range(1, 4):
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(random.randrange(3, 5))

            hrefs = browser.find_elements(By.TAG_NAME, 'a')
            posts_urls = [item.get_attribute('href') for item in hrefs if '/p/' in item.get_attribute('href')]

            for url in posts_urls:
                try:
                    browser.get(url)
                    time.sleep(10)
                    like_button = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button').click()
                    time.sleep(random.randrange(80, 120))
                except Exception as ex:
                    print(ex)
                    self.close_browser()