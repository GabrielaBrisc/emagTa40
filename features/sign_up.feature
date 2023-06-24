Feature: Check the sign up functionality

 Background:
   Given signUp: I am a user on the sign up page
   When signUp: Delete text from field

  @signUp
  Scenario Outline: Enter wrong email address and verify the error
    When signUp: I fill in the email field "<email>"
    When signUp: I click on Continue button
    Then signUp: I verify the error message "<error_message>"

    Examples:
      | email         | error_message |
      | test          | Email invalid |
      | test@yahoo    | Email invalid |
  @signUp
  Scenario: Check error message when input invalid name into "Numele si prenumele" field
    When signUp: I fill in the email field with valid data "brisc.gabriela1@yahoo.com"
    Then signUp: I click on continue button from login
    When signUp: I fill in the name "123"
    When signUp: I click on password field
    Then signUp: I verify the name error message "Numele și prenumele nu sunt valide"

  @signUp
  Scenario: Check error message when leave empty the fields
    When signUp: I fill in the email field data "brisc.gabriela1@yahoo.com"
    Then signUp: I click on Continue btn
    When signUp: I leave empty the Nume și prenume field
    When signUp: I leave empty the password field
    When signUp: I leave empty the confirm password field
    When signup: I click on register continue button from registration
    Then signUp: I verify the mandatory error message "Câmp obligatoriu"
