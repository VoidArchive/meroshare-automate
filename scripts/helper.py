from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class MeroShare:

    def __init__(self) -> None:
        option = webdriver.ChromeOptions()
        option.binary_location = r'/usr/bin/brave-browser'
        self.driver = webdriver.Chrome(executable_path=r'/home/archive/chromedriver_linux64/chromedriver', options=option)
        self.driver.maximize_window()

    def login(self, dp_name, user_name, password):
        self.driver.get("https://meroshare.cdsc.com.np/#/login")
        sleep(1)
        self.driver.find_element(
            By.CLASS_NAME, 'select2-selection__placeholder').click()
        # Depository Participant
        depository_Participant = self.driver.find_element(
            By.XPATH, '/html/body/span/span/span[1]/input')
        depository_Participant.send_keys(dp_name, Keys.ENTER)
        # Username
        username = self.driver.find_element(By.ID, 'username')
        username.send_keys(user_name)
        # Password
        user_password = self.driver.find_element(By.ID, 'password')
        user_password.send_keys(password, Keys.ENTER)

    def find_ipo(self, row):
        sleep(1)
        self.driver.get('https://meroshare.cdsc.com.np/#/asba')
        sleep(1)
        ipos = self.driver.find_elements(By.CLASS_NAME, 'btn-issue')
        ipos[row].click()

    def apply_ipo(self, applied_unit, crn):
        sleep(1)
        # Select Bank
        bank = self.driver.find_element(By.ID, 'selectBank')
        bank.click()
        bank.send_keys(Keys.ARROW_DOWN)
        bank.send_keys(Keys.ARROW_DOWN)
        bank.send_keys(Keys.ENTER)

        # Clear the field just in case
        applied_kitta = self.driver.find_element(By.ID, 'appliedKitta')
        applied_kitta.clear()
        applied_kitta.send_keys(applied_unit)

        self.driver.find_element(By.ID, 'crnNumber').send_keys(crn)

        self.driver.find_element(By.ID, 'disclaimer').click()

        sleep(2)
        self.driver.find_element(
            By.XPATH, '//*[@id="main"]/div/app-issue/div/wizard/div/wizard-step[1]/form/div[2]/div/div[5]/div[2]/div/button[1]').click()

    def enter_pin(self, transaction_password):
        sleep(1)
        self.driver.find_element(
            By.ID, 'transactionPIN').send_keys(transaction_password)

        sleep(1)
        self.driver.find_element(
            By.XPATH, '//*[@id="main"]/div/app-issue/div/wizard/div/wizard-step[2]/div[2]/div/form/div[2]/div/div/div/button[1]/span').click()

    def logout(self):
        sleep(2)
        self.driver.find_element(
            By.XPATH, '/html/body/app-dashboard/header/div[2]/div/div/div/ul/li[1]/a/i').click()

    def get_result(self):
        sleep(1)
        # company_name = self.driver.find_element(
        #     By.XPATH, '//*[@id="main"]/div/app-application-report/div/div[2]/div/div[1]/div/div/div/div/div/span[1]').text
        status = self.driver.find_element(
            By.XPATH, '//*[@id="main"]/div/app-application-report/div/div[2]/div/div[3]/div/div[1]/div[7]/div/div/div[2]/div/label').text

        # Exit
        sleep(1)
        self.driver.find_element(
            By.XPATH, '//*[@id="main"]/div/app-application-report/div/div[1]/div/div[1]/div/div/div/button/i').click()

        return status

    def check_ipo(self, row_no):
        sleep(1)
        self.driver.get('https://meroshare.cdsc.com.np/#/asba')
        self.driver.find_element(
            By.XPATH, '//*[@id="main"]/div/app-asba/div/div[1]/div/div/ul/li[3]/a/span').click()

        sleep(1)
        self.driver.find_element(
            By.XPATH, f'//*[@id="main"]/div/app-asba/div/div[2]/app-share-list/div/div/div[2]/div[1]/div[{str(row_no)}]/div/div[2]/div/div[3]/button').click()
       
