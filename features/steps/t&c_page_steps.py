from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


@given('Open Amazon T&C page')
def open_tcpage(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when("Store original windows")
def store_window(context):
    context.original_window = context.driver.current_window_handle
    print(context.driver.window_handles)
    print('Original window:', context.original_window)


@when('Click on Amazon Privacy Notice link')
def click_privacy(context):
    context.driver.find_element(By.XPATH, "//a[@href='https://www.amazon.com/privacy']").click()


@when("Switch to the newly opened window")
def switch_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    windows = context.driver.window_handles[1]
    context.driver.switch_to.window(windows)


@then("Verify Amazon Privacy Notice page is opened")
def verify_privacy_notice_opened(context):
    assert 'https://www.amazon.com/gp/help/customer/display.html?nodeId=GX7NJQ4ZB8MHFRNJ' in context.driver.current_url, f'Privacy Notice page did not opened'


@then("User can close new window and switch back to original")
def close_new_window(context):
    context.driver.close()
    context.driver.switch_to.window(context.original_window)


