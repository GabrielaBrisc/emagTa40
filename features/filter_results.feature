Feature: Check the filter functionality

  Background:
    @filter
    Scenario: I want to reach mobile phones screen
  Given filter: I am the user on homepage
  When filter: I click on accept preferences button
  When filter: I click on close btn from vezi oferta
  When filter: I hover over Laptop, Tablete & Telefoane
  When filter: I click on Telefoane mobile
      @filter
Scenario: I want to filter the results after pret crescator
  When filter: I click on cele mai populare dropdown
  Then filter: I click on pret crescator btn

#  Scenario: I want to filter by brand name
#  When filter: I click on Garmin filter from Brand
#  Then filter: I check if the list contains Garmin watches

  ### pot sa pun primi pasi ca si parte comuna si sa fac mai multe filtrari + verificari

