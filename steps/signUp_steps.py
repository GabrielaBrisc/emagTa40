from behave import *

#Enter wrong email address
@Given("signUp: I am a user on the sign up page")
def step_impl(context):
    context.signUp_page.navigate_to_login()

@When("signUp: Delete text from field")
def step_impl(context):
    context.signUp_page.delete_text_from_email_field()

@When('signUp: I fill in the email field "{email_address}"')
def step_impl(context, email_address):
    context.signUp_page.input_invalid_email(email_address)

@When("signUp: I click on Continue button")
def step_impl(context):
    context.signUp_page.click_continue_from_login()

@Then('signUp: I verify the error message "{email_error_msg}"')
def step_impl(context, email_error_msg):
    context.signUp_page.verify_error_message(email_error_msg)


#Check error message when input invalid name into "Numele si prenumele" field

@When('signUp: I fill in the email field with valid data "{email}"')
def step_impl(context, email):
    context.signUp_page.input_valid_email(email)

@Then("signUp: I click on continue button from login")
def step_impl(context):
    context.signUp_page.click_continue_btn()

@When('signUp: I fill in the name "{name}"')
def step_impl(context, name):
    context.signUp_page.fill_name_field(name)

@When("signUp: I click on password field")
def step_impl(context):
    context.signUp_page.click_pass_field()

@Then('signUp: I verify the name error message "{name_message}"')
def step_impl(context,name_message):
    context.signUp_page.verify_wrong_name_error(name_message)


#Check error message when leave empty the password field

@When('signUp: I fill in the email field data "{email}"')
def step_impl(context, email):
    context.signUp_page.input_valid_email(email)

@Then("signUp: I click on Continue btn")
def step_impl(context):
    context.signUp_page.click_continue_btn()
@When("signUp: I leave empty the Nume și prenume field")
def step_impl(context):
    context.signUp_page.leave_emty_nume_prenume_field()

@When("signUp: I leave empty the password field")
def step_impl(context):
    context.signUp_page.leave_empty_pass()

@When("signUp: I leave empty the confirm password field")
def step_impl(context):
    context.signUp_page.leave_empty_confirm_pass()

@When("signup: I click on register continue button from registration")
def step_impl(context):
    context.signUp_page.click_register_continue_btn()

@Then('signUp: I verify the mandatory error message "{mandatory_message}"')
def step_impl(context,mandatory_message):
    context.signUp_page.verify_mandatory_error(mandatory_message)