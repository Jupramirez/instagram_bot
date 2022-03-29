from lib2to3.pgen2 import driver
import time
from traceback import print_exception
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

#Se descarga e instala el driver que maneja el navegador
chrome_driver_path = r"CHROME_DRIVER_PATH"
#Se pasa como el ejecutable para chrome
driver = webdriver.Chrome(executable_path=chrome_driver_path)

#retardos para elementos
delay_login = 20 #segundos

# Abrir el navegador y maximiza la ventana
driver.get("https://www.instagram.com/")
# driver.maximize_window()



# try:
#     click_login = WebDriverWait(driver, delay_login). \
#     until(EC.presence_of_element_located((By.CSS_SELECTOR,".button[data-testid='appLoginBtn']")))
#     click_login.click()
# except TimeoutException:
#     print("Tomo mucho tiempo")

class InstaFollower:
    def __init__(self,driver):
        self.driver = driver
    
    def login_instagram(self):
        login = self.driver.find_element_by_name("username")
        login.send_keys("EMAIL")
        password = self.driver.find_element_by_name("password")
        password.send_keys("PASSWORD")
        password.send_keys(Keys.ENTER)
    
    def find_page(self):
        search = self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")
        search.send_keys("chefsteps")
        sleep(2)
        search.send_keys(Keys.DOWN)
        sleep(2)
        search.send_keys(Keys.ENTER)
        sleep(4)
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a/div").click()
    
    def find_followers(self):
        ul_followers = self.driver.find_element(By.XPATH,
        "/html/body/div[6]/div/div/div/div[2]")
        sleep(2)
        time_scroll = time.time() + 50
        while True:
            list_followers = self.driver.find_elements_by_css_selector(".PZuss li")
            for user in list_followers:
                try:
                    user.find_element(By.CSS_SELECTOR,"button").click()
                except:
                    self.driver.find_element(By.XPATH,
                    "/html/body/div[7]/div/div/div/div[3]/button[2]").click()
                sleep(2)
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight",ul_followers)
            if time.time() > time_scroll:
                break
            sleep(2)



instagram_bot = InstaFollower(driver)
sleep(10)
instagram_bot.login_instagram()
sleep(20)
instagram_bot.find_page()
sleep(15)
instagram_bot.find_followers()

print(instagram_bot)




# driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")
