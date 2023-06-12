from browser import Browser

# in aceasta pagina punem toate merode care sunt utile in orice pagina
# Si nu neaparat specifice doar unei pagini
class BasePage(Browser):

    def check_the_current_url(self,url):
        actual = self.driver.current_url
        assert actual == url, f"Url-ul este corect"