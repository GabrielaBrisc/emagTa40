from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import unittest

class AddToFavourite(BasePage):
    HEART_ICON = (By.XPATH, "//div[@class='card-item card-standard js-product-data'][1]/descendant::button[@class='add-to-favorites btn']") #de la ceasul dorit
    FAVORITE_BUTTON = (By.ID, "my_wishlist")
    ELEMENT_ADDED_TO_FAVOURITE = (By.XPATH, "//div[@class='product-card-account pad-sep-sm js-tracking-viewport-product  ']")
    OPEN_ITEM = (By.XPATH, "//div[@class='card-item card-standard js-product-data'][1]") #nu stiu sa il iau altfel
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
        self.driver.find_element(*self.ELEMENT_ADDED_TO_FAVOURITE).is_displayed()
        assert True

#   Scenario: I want to add an item to favourites after I open item's page
    def click_on_first_item_from_page(self):
        self.driver.find_element(*self.OPEN_ITEM).click()

    def click_on_heart_icon(self):
        self.driver.find_element(*self.HEART_ICON_FROM_ITEM_PAGE).click()