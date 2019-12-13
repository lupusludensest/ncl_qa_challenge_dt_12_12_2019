from pages.base_page import Page
from selenium.webdriver.common.by import By


class TopNavigation(Page):
    EXPLORE = (By.CSS_SELECTOR, "a.linkNav[title='Explore']")
    PORTS = (By.CSS_SELECTOR, "a.linkItem[title='Ports']")

    def click_explore(self):
        self.click(*self.EXPLORE)

    def click_ports(self):
        self.wait_for_element_click(*self.PORTS)
