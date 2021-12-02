# Created by Truong at 12/1/2021
Feature: Test Scenarios for help search functionality


  Scenario: User can search for solutions of Cancelling an order on Amazon
    Given Open Amazon help page
    When Input "Cancel order" into search field
    Then Verify that ‘Cancel Items or Orders’ text is present