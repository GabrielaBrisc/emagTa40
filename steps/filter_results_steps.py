from behave import *

@Given("filter: I am the user on homepage")
def step_impl(context):
    context.filter_results_page.navigate_to_homepage()
@When("filter: I click on accept preferences button")
def step_impl(context):
    context.filter_results_page.click_on_accept_preferences_btn()
@When("filter: I click on close btn from vezi oferta")
def step_impl(context):
    context.filter_results_page.click_on_close_btn_from_offer()
@When("filter: I hover over Laptop, Tablete & Telefoane")
def step_impl(context):
    context.filter_results_page.hover_on_laptop_tab_tel()

@When("filter: I click on Telefoane mobile")
def step_impl(context):
    context.filter_results_page.click_on_tel_mobile()


