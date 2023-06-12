from browser import Browser
from pages.signUp_page import SignUp
from pages.signIn_page import SignIn
from pages.search_page import Search
from pages.filter_results_page import Filter
from pages.add_to_favorites_page import AddToFavourite
from pages.add_to_cart_page import AddToCart

def before_all(context):
    context.browser = Browser() ## obj de tip browser
    context.signUp_page = SignUp()
    context.signIn_page = SignIn()
    context.search_page = Search()
    context.filter_results_page = Filter()
    context.add_to_favourites_page = AddToFavourite()
    context.add_delete_to_cart_page = AddToCart()

###dupa exe toate testele, vrem sa inchidem browser ul respectiv
def after_all(context):
    context.browser.close()