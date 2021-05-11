from selenium import webdriver
import time

class VoteBot():
    def __init__(self):
        self.driver = webdriver.Chrome("/usr/local/bin/chromedriver")

    def vote(self):
        self.driver.get('https://scorebooklive.com/washington/2021/05/10/vote-now-who-should-be-the-wafd-bank-washington-high-school-athlete-of-the-week-12/')
        #time.sleep(1)
        self.driver.find_element_by_xpath("//input[@name='PDI_answer10828700' and @value='49929094']").click()
        #time.sleep(1)
        self.driver.find_elements_by_xpath("//*[@id='pd-vote-button10828700']")[0].click()
        #time.sleep(1)
        self.driver.close()

while True:
    bot = VoteBot()
    bot.vote()