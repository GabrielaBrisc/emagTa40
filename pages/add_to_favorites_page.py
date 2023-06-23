from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AddToFavourite(BasePage):
    HEART_ICON = (By.XPATH, "//*[@id='card_grid']/div[1]/div/div/div[2]/button[1]/i") #de la ceasul dorit
    FAVORITE_BUTTON = (By.ID, "my_wishlist")
    ELEMENT_ADDED_TO_FAVOURITE = (By.XPATH, "//div[@class='product-card-account pad-sep-sm js-tracking-viewport-product  ']")
    OPEN_ITEM = (By.XPATH, "//a[@data-zone='title']") #nu stiu sa il iau altfel
    HEART_ICON_FROM_ITEM_PAGE = (By.XPATH,"//span[@class='gtm_t95ovv']")
    def nav_to_list_with_items(self):
        self.driver.get("https://www.emag.ro/search/smartwatch%20garmin%20dama?ref=effective_search")

    def click_favourite_icon(self):
        self.driver.find_element(*self.HEART_ICON).click()

    def click_on_favorite(self):
        self.driver.find_element(*self.FAVORITE_BUTTON).click()

    def check_the_current_url(self, url):
        actual_url = "https://www.emag.ro/favorites?ref=ua_favorites"
        assert url == actual_url, f'Error, the message is not in actual message, {actual_url}'

    def check_displayed_favourite_item(self):
       assert self.driver.find_element(*self.ELEMENT_ADDED_TO_FAVOURITE).is_displayed(), f"The element is displayed on favourite page"

#   Scenario: I want to add an item to favourites after I open item's page
    def click_on_first_item_from_page(self):
        list = self.driver.find_elements(*self.OPEN_ITEM)
        list[3].click()

    def click_on_heart_icon(self):
        self.driver.find_element(*self.HEART_ICON_FROM_ITEM_PAGE).click()