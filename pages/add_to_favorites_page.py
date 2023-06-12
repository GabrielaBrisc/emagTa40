from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AddToFavourite(BasePage):
    HEART_ICON = (By.XPATH, "//*[@id='card_grid']/div[1]/div/div/div[2]/button[1]/i") #de la ceasul dorit
    FAVORITE = (By.XPATH, "//*[@id='my_wishlist']/span[2]")
    FAVOURITE_ELEMENT = (By.XPATH,"//*[@id='list-of-favorites']/div")
    ITEM_LIST = (By.XPATH, "//a[@data-zone='title']")
    HEART_ICON_FROM_ITEM_PAGE = (By.XPATH,"//button[@class='add-to-favorites btn btn-xl btn-default btn-icon btn-block gtm_t95ovv']")

    def nav_to_list_with_items(self):
        self.driver.get("https://www.emag.ro/search/smartwatch%20garmin%20dama?ref=effective_search")

    def click_favourite_icon(self):
        self.driver.find_element(*self.HEART_ICON).click()

    def click_on_favorite(self):
        self.driver.find_element(*self.FAVORITE).click()

    def check_the_current_url(self, url):
        actual_url = "https://www.emag.ro/favorites?ref=ua_favorites"
        assert url == actual_url, f'Error, the message is not in actual message, {actual_url}'

    def check_displayed_favourite_item(self):
        self.driver.find_element(*self.FAVOURITE_ELEMENT).is_displayed()

#   Scenario: I want to add an item to favourites after I open item's page
    def click_on_first_item_from_page(self):
        list = self.driver.find_elements(*self.ITEM_LIST)
        list[3].click()

    def click_on_heart_icon(self):
        self.driver.find_element(*self.HEART_ICON_FROM_ITEM_PAGE).click()