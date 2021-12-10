from selenium.webdriver.common.by import By
from behave import given, when, then

PRODUCT_PRICE = (By.XPATH, "//a[.//span[@class='a-price']]")


@when('Click on the first product')
def click_first_product(context):
    context.driver.find_element(*PRODUCT_PRICE).click()


@then('Search results have {expected result}')
def verify_search_result(context, expected_result):
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']")
    assert actual_result == expected_result, f'Error, actual result {actual_result} did not match expected result {expected_result}'