Feature: Check the add to favorites functionality

  @addtofavourites
   Scenario: I want to add an item to favourite
     Given add_to_favourite: I am the user on the smartwatches list
     When add to favourite: I click on the heart icon from the wanted item
     When add to favourite: I click on the favorite section
     Then add to favourite: I verify the url "https://www.emag.ro/favorites?ref=ua_favorites"
     Then add to favourite: I verify if my item is displayed on the page

## add to favourites din pagina produsului