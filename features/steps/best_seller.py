from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

BEST_SELLER1 = (By.CSS_SELECTOR, "div._p13n-zg-nav-tab-all_style_zg-tabs-li-div__1YdPR")
BEST_SELLER2 = (By.CSS_SELECTOR, "div._p13n-zg-nav-tab-all_style_zg-tabs-li-selected-div__3tHnP")

@given('Open Amazon Best Seller page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')

@then('Verify that there are 5 links')
def verify_found_result_test(context):
    best_seller_link1 = context.driver.find_elements(*BEST_SELLER1)
    best_seller_link2 = context.driver.find_elements(*BEST_SELLER2)
    assert len(best_seller_link1) == 4 and len(best_seller_link2) == 1, f'Expected 5 links, but got {len(best_seller_link1)}+{len(best_seller_link2)} '


