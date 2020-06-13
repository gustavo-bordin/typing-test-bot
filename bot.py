from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import sys

class Bot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        self.driver.implicitly_wait(30)

    def enter_site(self):
        self.driver.get('https://10fastfingers.com/login')

    def login(self, email, passwd):
        self.driver.find_element_by_name('data[User][email]').send_keys(email)
        self.driver.find_element_by_name('data[User][password]').send_keys(passwd)
        self.driver.find_element_by_id('login-form-submit').click()

    def read_text(self):
        words = self.driver.find_elements_by_xpath("//div[@id='row1']/span")
        return words
    
    def answer_word(self, words):
        for word in words:
            word = word.text
            self.driver.find_element_by_id('inputfield').send_keys(word)
            self.driver.find_element_by_id('inputfield').send_keys(Keys.SPACE)

email = sys.argv[1]
passwd = sys.argv[2]

bot = Bot()
bot.enter_site()
bot.login(email, passwd)
while(True):
    words = bot.read_text()
    bot.answer_word(words)