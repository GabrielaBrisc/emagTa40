from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SignIn(BasePage):
    EMAIL_FIELD = (By.ID,"user_login_email")
    LOGIN_CONTINUE_BTN = (By.ID, "user_login_continue")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='user_login[password]']")
    REMEMBER_ME_BTN = (By.ID,"remember_me")

    def navigate_to_sign_in(self):
        self.driver.get("https://auth.emag.ro/user/login")

    def input_email_address(self, email_address):
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email_address)

    def click_login_continue_btn(self):
        self.driver.find_element(*self.LOGIN_CONTINUE_BTN).click()

    def input_password(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)

    # def click_remember_me_checkbox(self):
    #     self.driver.find_element(*self.REMEMBER_ME_BTN).click()

    def click_continue_from_password(self):
        self.driver.find_element(*self.LOGIN_CONTINUE_BTN).click()
