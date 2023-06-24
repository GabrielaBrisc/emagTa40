from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver import Keys

class Search(BasePage):
    SEARCH_FIELD = (By.ID,"searchboxTrigger")
    SMARTWATCHES_LIST = (By.XPATH, "//div[@class='card-item card-standard js-product-data']/descendant::a[@class='card-v2-title semibold mrg-btm-xxs js-product-url']")

    def navigate_to_emag_page(self):
        self.driver.get("https://www.emag.ro/")

    def input_searched_item(self, item):
        self.driver.find_element(*self.SEARCH_FIELD).send_keys(item)

    def hit_enter(self):
        self.driver.find_element(*self.SEARCH_FIELD).send_keys(Keys.ENTER)

    def verify_if_search_is_correct(self):
        element = self.driver.find_elements(*self.SMARTWATCHES_LIST)
        search_text = "Smartwatch"
        contains_text = True
        if search_text in element:
            print(f"The element contains the {search_text}.")
        else:
            contains_text = False
            print(f"The element does not contain the search text: {search_text}.")
        assert contains_text == False, f'Error, the search did not returned smartwatches'