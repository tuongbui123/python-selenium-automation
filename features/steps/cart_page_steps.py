from selenium.webdriver.common.by import By
from behave import given, when, then

CART = (By.ID,"nav-cart-count")


@when('Open cart page')
def open_cart_page(context):
    context.driver.find_element(By.ID, "nav-cart").click()


@then('Verify cart has {expected_count} item(s)')
def verify_cart_count(context , expected_count):
    actual_count = context.driver.find_element(*CART).text
    assert actual_count == expected_count, f'Error, actual {actual_count} did not match expected {expected_count}'

