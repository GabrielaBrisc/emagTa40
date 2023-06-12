from behave import *

@Given("filter: I am the user on homepage")
def step_impl(context):
    context.filter_results_page.navigate_to_homepage()
@When("filter: I click on accept preferences button")
def step_impl(context):
    try:
        context.filter_results_page.click_on_accept_preferences_btn()
    except Exception as error:  # Exception prinde orice eroare poate aparea in blocul de try:
        print(error)

@When("filter: I click on close btn from vezi oferta")
def step_impl(context):
    try:
        context.filter_results_page.click_on_close_btn_from_offer()
    except Exception as error:
        print(error)

@When("filter: I hover over Laptop, Tablete & Telefoane")
def step_impl(context):
    context.filter_results_page.hover_on_laptop_tab_tel()

@When("filter: I click on Telefoane mobile")
def step_impl(context):
    context.filter_results_page.click_on_tel_mobile()

# Scenario: I want to filter the results after pret crescator
@When("filter: I click on cele mai populare dropdown")
def step_impl(context):
    context.filter_results_page.click_on_cele_mai_populare_dropdown()
@Then("filter: I click on pret crescator btn")
def step_impl(context):
    context.filter_results_page.click_on_pret_crescator()


