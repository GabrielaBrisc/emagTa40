Feature: Check search functionality
  @search
  Scenario: I search for an item
    Given search: I am a user on emag page
    When search: I click on search field and input "smartwatch"
    Then search: I hit the enter button from keyboard and some results are displayed


