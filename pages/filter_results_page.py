from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class Filter(BasePage):

    LAPTOPURI_TELEFOANE_LINK = (By.XPATH, "//span[contains(text(),'Laptop')]/parent::a[@class='js-megamenu-list-department-link gtm_31vgamc']")
    TELEFOANE_ACCESORII = (By.LINK_TEXT, "Telefoane mobile & accesorii")
    ACCEPT_PREFERENCES = (By.CSS_SELECTOR,"button[class='btn btn-primary js-accept gtm_h76e8zjgoo btn-block']")
    CLOSE_BTN_VEZI_OFERTA = (By.XPATH, "//button[@class='close']")
    TELEFOANE_MOBILE = (By.CSS_SELECTOR,"a[data-id='4835']")
    PREFERENCES_BANNER = (By.XPATH,"//div[@class='gdpr-cookie-banner js-gdpr-cookie-banner pad-sep-xs pad-hrz-none show']")
    CELE_MAI_POPULARE_DROPDOWN = (By.XPATH,"//span[contains(text(),'Cele mai populare')][@class='sort-control-btn-option text-truncate']")
    PRET_CRESCATOR = (By.XPATH,"//a[@data-sort-dir='asc']")

    def navigate_to_homepage(self):
        self.driver.get("https://www.emag.ro/")
    def click_on_accept_preferences_btn(self):
            self.driver.find_element(*self.ACCEPT_PREFERENCES).click()

    def click_on_close_btn_from_offer(self):
            self.driver.find_element(*self.CLOSE_BTN_VEZI_OFERTA).click()

    def hover_on_laptop_tab_tel(self):
        #nu face hover?
        elem_hover = self.driver.find_element(*self.LAPTOPURI_TELEFOANE_LINK)
        action = ActionChains(self.driver)
        action.move_to_element(elem_hover).perform()

    def click_on_tel_mobile(self):
        self.driver.find_element(*self.TELEFOANE_MOBILE).click()

# Scenario: I want to filter the results after pret crescator
    def click_on_cele_mai_populare_dropdown(self):
        self.driver.find_element(*self.CELE_MAI_POPULARE_DROPDOWN).click()

    def click_on_pret_crescator(self):
        self.driver.find_element(*self.PRET_CRESCATOR).click()

