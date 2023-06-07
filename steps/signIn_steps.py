from behave import  *

@Given("signIn: I am a user on the sign in page")
def step_impl(context):
    context.signIn_page.navigate_to_sign_in()

@When('signIn: I fill in the email field with valid address "{email_address}"')
def step_impl(context, email_address):
    context.signIn_page.input_email_address(email_address)

@When("signIn: I click on Continue btn")
def step_impl(context):
    context.signIn_page.click_login_continue_btn()

@When('signIn: I fill in the password field "{password}"')
def step_impl(context, password):
    context.signIn_page.input_password(password)

# @When("signIn: I click on remember me checkbox")
# def step_impl(context):
#     context.signIn_page.click_remember_me_checkbox()

@Then("signIn: I click on continue button from login screen")
def step_impl(context):
    context.signIn_page.click_continue_from_password()
