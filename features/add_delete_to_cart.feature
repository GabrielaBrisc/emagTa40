Feature: Check add to cart functionality
  @additem
  Scenario: I want to add an item to cart
  Given add_to_cart: I am a user on the emag page
  When add_to_cart: I click on the desired item
  Then add_to_cart: I click on add to cart btn
