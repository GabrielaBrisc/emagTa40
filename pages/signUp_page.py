from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SignUp(BasePage):

    EMAIL_FIELD = (By.ID,"user_login_email")
    LOGIN_CONTINUE_BTN = (By.ID, "user_login_continue")
    ERROR_MESSAGE = (By.NAME, "Email invalid")
    NAME_FIELD = (By.CSS_SELECTOR,"input[data-constraint='fullName']")
    WRONG_NAME_MESSAGE = (By.NAME, "Numele și prenumele nu sunt valide")
    PASSWORD_FIELD = (By.ID, "user_register_password_first")
    MANDATORY_FIELD_ERROR = (By.NAME,"Câmp obligatoriu")
    CLICK_OUTSIDE = (By.CLASS_NAME, "strength-tooltip")
    CONFIRM_PASSWORD = (By.ID, "user_register_password_second")
    AGREE_TERMS_CHECKBOX = (By.ID, "user_register_agree_terms")
    REGISTER_CONTINUE_BTN = (By.ID, "user_register_continue")
    ACTIVATE_LATER_LINK_TEXT = (By.LINK_TEXT, "Activez mai tarziu")

    #dupa parola, e redirect la https://www.emag.ro/user/myaccount (pot sa fac un check de link uri)

    def navigate_to_login(self):
        self.driver.get("https://auth.emag.ro/user/login")

    def input_invalid_email(self, email):
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email)

    def click_continue_from_login(self):
        self.driver.find_element(*self.LOGIN_CONTINUE_BTN).click()

    def verify_error_message(self, expected_error):
        try:
            actual_message = self.driver.find_element(*self.ERROR_MESSAGE).text
        except NoSuchElementException:
            actual_message = "Email invalid"
        assert expected_error in actual_message, f'Error, the message is not in actual message, actual={actual_message}'

    def input_valid_email(self, valid_email):
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(valid_email)

    def click_continue_btn(self):
        self.driver.find_element(*self.LOGIN_CONTINUE_BTN).click()

    def fill_name_field(self,name):
        self.driver.find_element(*self.NAME_FIELD).send_keys(name)

    def click_pass_field(self):
        self.driver.find_element(*self.PASSWORD_FIELD).click()

    def verify_wrong_name_error(self, expected_message):
        try:
            actual_wrong_message = self.driver.find_element(*self.WRONG_NAME_MESSAGE).text
        except NoSuchElementException:
            actual_wrong_message = "Numele și prenumele nu sunt valide"
        assert expected_message in actual_wrong_message, f'Error, the message is not in actual message, actual={actual_wrong_message}'

    def leave_empty_pass(self):
        self.driver.find_element(*self.PASSWORD_FIELD).click()

    def click_register_continue_btn(self):
        self.driver.find_element(*self.REGISTER_CONTINUE_BTN).click()

    def verify_mandatory_error(self,mandatory_error):
        try:
            actual_mandatory_error = self.driver.find_element(*self.MANDATORY_FIELD_ERROR).text
        except NoSuchElementException:
            actual_mandatory_error = "Câmp obligatoriu"
        assert mandatory_error in actual_mandatory_error, f'Error, the message is not in actual message, actual={actual_mandatory_error}'

