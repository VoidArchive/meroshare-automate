from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep

MEROSHARE_URL = 'https://meroshare.cdsc.com.np'
APPLY_UNIT = 10


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
            print('Connecting to Meroshare.......')
            self.wait.until(EC.presence_of_element_located(
                (By.ID, 'username')))
        except TimeoutException:
            print('Could not load Meroshare..')
            self.browser.quit()
            self.browser.close()

    def login(self, name, depository, username, password):
        sleep(1)
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

            print(f'Loged In By: {name}')
            self.browser.get(f'{MEROSHARE_URL}/#/asba')
        except TimeoutException:
            self.browser.close()

    def show_offering(self):
        # This fuction depends on login function as you cannot view ipo without loging In.
        try:
            # Check If My ASBA has been loaded
            company_name = self.wait.until(EC.presence_of_all_elements_located(
                (By.CLASS_NAME, 'company-name')))

            for i in range(len(company_name)):
                offering = company_name[i].text.split('\n')
                offering = " ".join(offering)
                print(f"{i}. {offering}")
        except TimeoutException:
            print('No offering available')
            self.browser.quit()
            # self.browser.close()

    def get_offering(self, offer_row):
        # The maybe "Apply", "Edit", Or None

        offering_btn = self.wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'btn-issue')))

        if offering_btn[offer_row].text == "Apply":
            offering_btn[offer_row].click()
        elif offering_btn[offer_row].text == "Edit":
            print("You have already applied to this IPO.")
        else:
            print("You are not allowed to apply for this IPO.")

    def apply_offering(self, crn, pin):

        # Select Bank
        bank = self.wait.until(
            EC.presence_of_element_located((By.ID, 'selectBank')))
        bank.click()
        bank.send_keys(Keys.ARROW_DOWN)
        bank.send_keys(Keys.ARROW_DOWN)
        bank.send_keys(Keys.ENTER)

        # Apply share unit -> 10 default
        apply_unit = self.browser.find_element(By.ID, 'appliedKitta')
        # Clear the field just in case
        apply_unit.clear()
        apply_unit.send_keys(APPLY_UNIT)

        # Enter CRN
        self.browser.find_element(By.ID, 'crnNumber').send_keys(crn)

        # Check the disclaimer
        self.browser.find_element(By.ID, 'disclaimer').click()

        # Wait for Proceed Button to be Enable
        self.wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="main"]/div/app-issue/div/wizard/div/wizard-step[1]/form/div[2]/div/div[5]/div[2]/div/button[1]'))).click()

        # Enter Transaction Pin
        self.wait.until(EC.presence_of_element_located(
            (By.ID, 'transactionPIN'))).send_keys(pin)
        # Wait for Apply Button to be Enabled TODO: ADD .click()
        self.wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="main"]/div/app-issue/div/wizard/div/wizard-step[2]/div[2]/div/form/div[2]/div/div/div/button[1]')))

    def logout(self):
        self.wait.until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/app-dashboard/header/div[2]/div/div/div/ul/li[1]/a'))).click()

    def get_result(self, offer_row) -> str:
        # Go to Application Report
        self.wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="main"]/div/app-asba/div/div[1]/div/div/ul/li[3]/a/span'))).click()

        reports = self.wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'btn-issue')))
        reports[offer_row].click()

        # Get Status
        sleep(1)
        company_name = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="main"]/div/app-application-report/div/div[2]/div/div[1]/div/div/div/div/div/span[1]')))
        status = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="main"]/div/app-application-report/div/div[2]/div/div[3]/div/div[1]/div[7]/div/div/div[2]/div/label')))

        return f'{company_name.text}: {status.text}'
