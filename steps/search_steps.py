from behave import *

@Given("search: I am a user on emag page")
def step_impl(context):
    context.search_page.navigate_to_emag_page()

@When('search: I click on search field and input "{search_item}"')
def step_impl(context, search_item):
    context.search_page.input_searched_item(search_item)

@Then("search: I hit the enter button from keyboard and some results are displayed")
def step_impl(context):
    context.search_page.hit_enter()