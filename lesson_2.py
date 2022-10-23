from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from auth_date import username, password
import time
import random


def hashtag_serch(username, password, hashtag):

    browser = webdriver.Chrome(r'C:\Python\Instagram_Bot\chromedriver\chromedriver')

    try:
        browser.get('https://www.instagram.com')
        time.sleep(random.randrange(3, 5))

        username_input = browser.find_element(By.NAME, 'username')
        username_input.clear()
        username_input.send_keys(username)

        time.sleep(2)

        password_input = browser.find_element(By.NAME, 'password')
        password_input.clear()
        password_input.send_keys(password)

        password_input.send_keys(Keys.ENTER)
        time.sleep(20)

        try:
            browser.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
            time.sleep(10)

            hrefs = browser.find_elements(By.TAG_NAME, 'a')

            posts_urls = [item.get_attribute('href') for item in hrefs if '/p/' in item.get_attribute('href')]

            # posts_urls = []
            # for item in hrefs:
            #     href = item.get_attribute('href')
            #     if '/p/' in href:
            #         posts_urls.append(href)
            #         print(href)

            for url in posts_urls[0:1]:
                browser.get(url)
                like_button = browser.find_element(By.XPATH, '//*[@id="mount_0_0_iw"]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button/div[2]/span/svg').click()
                time.sleep(10)

            browser.close()
            browser.quit()

        except Exception as ex:
            print(ex)
            browser.close()
            browser.quit()

    except Exception as ex:
        print(ex)
        browser.close()
        browser.quit()


hashtag_serch(username, password, 'watch')