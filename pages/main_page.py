from pages.base_page import Page


class MainPage(Page):

    def open(self):
        self.open_page('https://www.amazon.com/')
