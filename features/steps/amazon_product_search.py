from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.CSS_SELECTOR, 'input#twotabsearchtextbox')
SEARCH_SUBMIT = (By.CSS_SELECTOR, 'input#nav-search-submit-button')





@when('Search for {search_word}')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(search_word)
    sleep(4)


@when('Click search icon')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_SUBMIT).click()
    sleep(1)


