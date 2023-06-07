from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class Filter(BasePage):

    ELECTRICE_LINK = (By.LINK_TEXT,"Laptop, Tablete & Telefoane")
    TELEFOANE_ACCESORII = (By.LINK_TEXT, "Telefoane mobile & accesorii")
    TELEFOANE_MOBILE = (By.CSS_SELECTOR,"a[data-id='4835']")
#"//*[@id='emg-body-overlay']/div[2]/div[2]/div/div[3]/aside/ul[1]/li[1]/a")

    def navigate_to_homepage(self):
        self.driver.get("https://www.emag.ro/")

    def hover_on_laptop_tab_tel(self):
        #nu face hover?

        elem_hover = self.driver.find_element(*self.ELECTRICE_LINK)
        action = ActionChains(*self.ELECTRICE_LINK)
        action.move_to_element(elem_hover)

    def click_on_tel_mobile(self):
        self.driver.find_element(*self.TELEFOANE_MOBILE).click()
    #
    # def click_on_tel_mobile(self):
    #     self.driver.find_element(*self.TELEFOANE_MOBILE)

