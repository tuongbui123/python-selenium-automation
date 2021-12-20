# Created by Svetlana at 4/4/19
Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Google page
    When Input Watches into search field
    And Click on search icon
    Then Product results for Watches are shown


  Scenario: User can add a product to the cart
    Given Open Amazon page
    When Search for jacket
    And Click search icon
    And Click on the first product
    And Click on Add to cart button
    And Open cart page
    Then Verify cart has 1 item(s)