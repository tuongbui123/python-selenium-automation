from selenium.webdriver.common.by import By
from behave import given, when, then

ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
COLOR_OPTIONS = (By.CSS_SELECTOR,'#variation_color_name li')
SELECTED_COLOR = (By.CSS_SELECTOR,'#variation_color_name .selection')

@given('Open Amazon product {product_id} page')
def open_amazon_product(context , product_id):
    context.driver.get(f'https://www.amazon.com/gp/product/{product_id}')


@when('Click on Add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()


@then('Verify user can click through colors')
def verify_can_click_colors(context):
    expected_colors = ['LR Black', 'LR Green', 'LR Red', 'LR Violet']

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for i in range(len(colors)):
        colors[i].click()
        actual_color = context.driver.find_element(*SELECTED_COLOR).text

        assert actual_color == expected_colors[i], f'Expected {expected_colors[i]}, but got {actual_color}'