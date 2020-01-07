from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        self.base_url = 'https://www.ncl.com/'

    def click(self, *locator):
        """
        Clicks on WebElement
        :param locator: search strategy for find_element of a Web Element.
        """
        self.driver.find_element(*locator).click()

    def open_page(self, url: str=''):
        self.driver.get(self.base_url + url)

    def input_text(self, text: str, *locator):
        """
        :param text: Text to input
        :param locator: search strategy for find_element of a Web Element.
        """
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def wait_for_element_click(self, *locator):
        e = self.wait.until(EC.element_to_be_clickable(locator))
        e.click()

    def wait_for_element_appear(self, *locator):
        self.wait.until(EC.presence_of_element_located(locator))
