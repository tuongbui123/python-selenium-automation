# Created by Truong at 1/30/2022
Feature:  Logged out user sees Sign in page when clicking Orders


  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click Amazon Orders link
    Then Verify Sign In page is opened