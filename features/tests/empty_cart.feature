# Created by Truong at 12/1/2021
Feature: Test Scenarios for shopping cart functionality


  Scenario: Verify Amazon cart is empty
    Given Open Amazon page
    When Click on cart icon
    Then Verify that ‘Your Amazon Cart is empty’ text is present