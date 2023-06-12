Feature: Check the filter functionality

  Background:
    @filter
    Scenario:
  Given filter: I am the user on homepage
  When filter: I click on accept preferences button
  When filter: I click on close btn from vezi oferta
  When filter: I hover over Laptop, Tablete & Telefoane
  When filter: I click on Telefoane mobile

Scenario: I want to filter the results after pret crescator
  When filter: I click on cele mai populare dropdown
  Then filter: I click on pret crescator btn


  ### pot sa pun primi pasi ca si parte comuna si sa fac mai multe filtrari + verificari

