from selenium import webdriver


class Browser:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.set_page_load_timeout(15)

    def close(self):
        self.driver.quit()