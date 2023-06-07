from browser import Browser
from pages.signUp_page import SignUp
from pages.signIn_page import SignIn
from pages.search_page import Search
from pages.filter_results_page import Filter

def before_all(context):
    context.browser = Browser() ## obj de tip browser
    context.signUp_page = SignUp()
    context.signIn_page = SignIn()
    context.search_page = Search()
    context.filter_results_page = Filter()

###dupa exe toate testele, vrem sa inchidem browser ul respectiv
def after_all(context):
    context.browser.close()