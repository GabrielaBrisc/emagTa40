from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver import Keys

class Search(BasePage):
    SEARCH_FIELD = (By.ID,"searchboxTrigger")

    def navigate_to_emag_page(self):
        self.driver.get("https://www.emag.ro/")

    def input_searched_item(self, item):
        self.driver.find_element(*self.SEARCH_FIELD).send_keys(item)

    def hit_enter(self):
        self.driver.find_element(*self.SEARCH_FIELD).send_keys(Keys.ENTER)