# Created by Truong at 12/9/2021
Feature: Test scenario for adding item to cart functionality

Scenario: User can add a product to the cart
    Given Open Amazon page
    When Search for jacket
    And Click search icon
    And Click on the first product
    And Click on Add to cart button
    And Open cart page
    Then Verify cart has 1 item(s)