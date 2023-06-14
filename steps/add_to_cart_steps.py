from behave import *
@Given("add_to_cart: I am a user on the emag page")
def step_impl(context):
    context.add_to_cart_page.navigate_to_page()
@When("add_to_cart: I click on the desired item")
def step_impl(context):
    context.add_to_cart_page.click_on_item()
@Then("add_to_cart: I click on add to cart btn")
def step_impl(context):
    context.add_to_cart_page.click_add_to_cart()


