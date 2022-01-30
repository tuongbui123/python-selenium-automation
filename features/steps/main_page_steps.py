from selenium.webdriver.common.by import By
from behave import given, when, then

@when("Click Amazon Orders link")
def open_orders_link(context):
    context.app.header.click_order()


@then('Verify Sign in page is opened')
def verify_found_results_text(context, expected_result):
    actual_result = context.driver.find_element(By.ID, "ap_email")
    assert expected_result == actual_result, f'Error, actual result {actual_result} did not match expected result {expected_result}'