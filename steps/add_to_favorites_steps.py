from behave import  *
@Given("add_to_favourite: I am the user on the smartwatches list")
def step_impl(context):
    context.add_to_favourites_page.nav_to_list_with_items()

@When("add to favourite: I click on the heart icon from the wanted item")
def step_impl(context):
    context.add_to_favourites_page.click_favourite_icon()

@When("add to favourite: I click on the favorite section")
def step_impl(context):
    context.add_to_favourites_page.click_on_favorite()

@Then('add to favourite: I verify the url "{favourites_url}"')
def step_impl(context, favourites_url):
    context.add_to_favourites_page.check_the_current_url(favourites_url)

@Then("add to favourite: I verify if my item is displayed on the page")
def step_impl(context):
    context.add_to_favourites_page.check_displayed_favourite_item()

#   Scenario: I want to add an item to favourites after I open item's page
@When("add to favourite: I click on the first item from the list")
def step_impl(context):
    context.add_to_favourites_page.click_on_first_item_from_page()

@Then("add to favourite: I click on the heart icon to add it to favourites")
def step_impl(context):
    context.add_to_favourites_page.click_on_heart_icon()