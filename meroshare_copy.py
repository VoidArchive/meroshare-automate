from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


MEROSHARE_URL = 'https://meroshare.cdsc.com.np'


class MeroShare:
    def __init__(self) -> None:
        options = webdriver.ChromeOptions()
        options.binary_location = r'/usr/bin/brave-browser'
        options.add_argument("--incognito")
        # options.add_argument("--headless")
        self.browser = webdriver.Chrome(
            executable_path=r'/home/void/chromedriver_linux64/chromedriver', options=options)
        self.browser.maximize_window()
        self.wait = WebDriverWait(self.browser, 10)
        try:
            self.browser.get(MEROSHARE_URL)
            print('Connecting Meroshare.')
            self.wait.until(EC.presence_of_element_located(
                (By.ID, 'username')))
        except TimeoutException:
            print('Could not load Meroshare..')
            self.browser.quit()
            self.browser.close()

    def login(self, name, depository, username, password):
        try:
            # Enter Depository participant
            self.browser.find_element(
                By.CLASS_NAME, 'select2-selection__rendered').click()
            self.browser.find_element(
                By.CLASS_NAME, 'select2-search__field').send_keys(depository, Keys.ENTER)

            # Enter username and password
            self.browser.find_element(By.ID, 'username').send_keys(username)
            self.browser.find_element(
                By.ID, 'password').send_keys(password, Keys.ENTER)

            # Check if Login in succesful
            self.wait.until(EC.presence_of_element_located(
                (By.CLASS_NAME, 'user-profile-name')))

            print(f'Loged In: {name}')
        except TimeoutException:
            print(f'Could not Log In: {name}')
            self.browser.quit()
            self.browser.close()

    def get_offering(self):
        try:
            self.browser.get(f'{MEROSHARE_URL}/#/asba')
            # Check If My ASBA has been loaded
            company_list = self.wait.until(EC.presence_of_all_elements_located(
                (By.CLASS_NAME, 'company-list')))

            a = company_list[0].text.split()
            print(a)

        except TimeoutException:
            print('Could not find MY ASBA')
            self.browser.quit()
            # self.browser.close()
