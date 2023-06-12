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
    ORDER_BY_PRICE = (By.NAME,"Pret crescator")

    def navigate_to_homepage(self):
        self.driver.get("https://www.emag.ro/")
    def click_on_accept_preferences_btn(self):
        try:
            self.driver.find_element(*self.ACCEPT_PREFERENCES).click()
        except Exception as error:  # Exception prinde orice eroare poate aparea in blocul de try:
            print(error)

    def click_on_close_btn_from_offer(self):
        try:
            self.driver.find_element(*self.CLOSE_BTN_VEZI_OFERTA).click()
        except Exception as error:
            print(error)


    def hover_on_laptop_tab_tel(self):
        #nu face hover?
        elem_hover = self.driver.find_element(*self.LAPTOPURI_TELEFOANE_LINK)
        action = ActionChains(self.driver)
        action.move_to_element(elem_hover).perform()

    def click_on_tel_mobile(self):
        self.driver.find_element(*self.TELEFOANE_MOBILE).click()


