from selenium.webdriver.common.by import By

from pages.base_page import Page


class Header(Page):
    CLICK_ORDERS = (By.ID, "nav-link-accountList")
    CLICK_CART = (By.XPATH, "//a[@href='/gp/cart/view.html?ref_=nav_cart' and @id='nav-cart']")

    def click_order(self):
        self.click(*self.CLICK_ORDERS)

    def click_cart(self):
        self.click(*self.CLICK_CART)