Feature: Check the add to favorites functionality

  Background:
     Given add_to_favourite: I am the user on the smartwatches list

  @addtofavourites
   Scenario: I want to add an item to favourite
     When add to favourite: I click on the heart icon from the wanted item
     When add to favourite: I click on the favorite section
     Then add to favourite: I verify the url "https://www.emag.ro/favorites?ref=ua_favorites"
     Then add to favourite: I verify if my item is displayed on the page

  @addtofavourites
   Scenario: I want to add an item to favourites after I open item's page
     When add to favourite: I click on the first item from the list
     Then add to favourite: I click on the heart icon to add it to favourites