from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.keys import Keys

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on cart icon')
def input_search(context):
    search = context.driver.find_element(By.XPATH, "//a[@href='/gp/cart/view.html?ref_=nav_cart' and @id='nav-cart']")
    search.click()


@then('Verify that ‘Your Amazon Cart is empty’ text is present')
def verify_found_results_text(context):
    element = context.driver.find_element(By.XPATH, "//h2['Your Amazon Cart is empty']")
    assert 'Your Amazon Cart is empty' == element.text, f"Expected text not in {context.driver.current_url.lower()}"
