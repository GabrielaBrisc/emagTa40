from selenium.webdriver.common.by import By
from pages.base_page import BasePage
class AddToCart(BasePage):
    ITEM = (By.XPATH,"//div//h2[@class='card-v2-title-wrapper']//a[1]")
    ADD_TO_CART_BTN = (By.XPATH,"//button[@class='btn btn-xl "
    "btn-primary btn-emag btn-block main-button gtm_680klw yeahIWantThisProduct']")
    def navigate_to_page(self):
        self.driver.get("https://www.emag.ro/search/smartwatch%20dama?ref=effective_search")
    def click_on_item(self):
        self.driver.find_element(*self.ITEM).click()
    def click_add_to_cart(self):
        self.driver.find_element(*self.ADD_TO_CART_BTN).click()
