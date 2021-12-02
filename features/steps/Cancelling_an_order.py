from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.keys import Keys


@given('Open Amazon help page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@when('Input "Cancel order" into search field')
def input_search(context):
    search = context.driver.find_element(By.XPATH, "//input[@type='search' and @id='helpsearch']")
    search.send_keys('Cancel order')
    sleep(2)
    search.send_keys(Keys.RETURN)


@then('Verify that ‘Cancel Items or Orders’ text is present')
def verify_found_results_text(context):
    element = context.driver.find_element(By.XPATH, "//h1['Cancel Items or Orders']")
    assert 'Cancel Items or Orders' == element.text, f"Expected query not in {context.driver.current_url.lower()}"