from pages.base_page import Page
from selenium.webdriver.common.by import By


class ShoreExcursions(Page):
    NAV_EXCURSIONS = (By.CSS_SELECTOR, "button.btn-cta.btn-primary.btn-large.search-submit")
    SH_EXC_IS_PRESENT = (By.CSS_SELECTOR, "h2.header-title.visible-desktops")

    def click_find_excursions(self):
        self.wait_for_element_click(*self.NAV_EXCURSIONS)

    def text_is_present(self):
        self.text_is_present(*self.SH_EXC_IS_PRESENT)