class Page:

    def __init__(self, driver):
        self.driver = driver

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def open_page(self, url):
        self.driver.get(url)

    