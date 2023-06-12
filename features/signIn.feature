Feature: Check the sign in functionality
  Background:
    Given signIn: I am a user on the sign in page
  @signin
  Scenario: Enter valid email address and password
    When signIn: I fill in the email field with valid address "fgert.dfs@sd.cp"
    When signIn: I click on Continue btn
    When signIn: I fill in the password field "Gabriela*"
    When signIn: I click on remember me checkbox
    Then signIn: I click on continue button from login screen

