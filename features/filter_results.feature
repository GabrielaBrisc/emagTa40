Feature: Check the filter functionality
@filter
Scenario: I want to filter the results
  Given filter: I am the user on homepage
  When filter: I hover over Laptop, Tablete & Telefoane
  When filter: I click on Telefoane mobile
#  Then filter: I click on Telefoane mobile
# //div[@class="megamenu-group collapse megamenu-group-3999"]/a[1] -pt tel pe modala

 # assertions sa verific daca modala aia de