from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "Your email"
TWITTER_PASSWORD = "Your password"
TWITTER_LOGIN = "Your login"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.s = Service("C:/Users/USER/Downloads/chromedriver_win32/chromedriver.exe")
        self.options = webdriver.ChromeOptions()
        self.browser = webdriver.Chrome(options=self.options, service=self.s)
        self.url = "https://www.speedtest.net/"
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.browser.get(self.url)
        time.sleep(3)
        self.browser.find_element(By.ID, "onetrust-accept-btn-handler").click()
        self.browser.find_element(By.CSS_SELECTOR, ".start-button a").click()
        time.sleep(60)
        self.up = float(
            self.browser.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/di'
                                                'v[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/'
                                                'span').text)
        self.down = float(
            self.browser.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]'
                                                '/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]'
                                                '/span').text)
        print(f"Up: {self.up}\nDown: {self.down}")

    def tweet_at_provider(self):
        self.browser.get("https://twitter.com/login")
        time.sleep(5)
        email = self.browser.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div'
                                                    '/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email.click()
        email.send_keys(TWITTER_EMAIL)
        email.send_keys(Keys.ENTER)
        time.sleep(5)
        login = self.browser.find_element(By.NAME, 'text')
        login.click()
        login.send_keys(TWITTER_LOGIN)
        login.send_keys(Keys.ENTER)
        time.sleep(5)
        password = self.browser.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div'
                                                       '/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div'
                                                       '[1]/input')
        password.click()
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)
        time.sleep(3)
        write_a_tweet = self.browser.find_element(By.XPATH,
                                                  '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div['
                                                  '1]/div[3]/a')
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for" \
                f" {PROMISED_DOWN}down/{PROMISED_UP}up?"
        write_a_tweet.click()
        time.sleep(3)
        draft = self.browser.find_element(By.XPATH, "//div[@role='textbox']")
        draft.click()
        draft.send_keys(tweet)
        time.sleep(3)
        self.browser.find_element(By.XPATH, "//div[@data-testid='tweetButton']").click()
        time.sleep(2)


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
