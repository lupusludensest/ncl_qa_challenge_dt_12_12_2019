from pages.base_page import Page
from selenium.webdriver.common.by import By


class PortOfCall(Page):
    SEARCH_BAR = (By.ID, 'searchbar')
    FOUND_PORT_LIST_ITEM = (By.CSS_SELECTOR, 'ul.list-find-port')
    PLUS_ZOOMED_IN = (By.CSS_SELECTOR, "li.control-zoom-in[style='opacity: 0.5;']") # opacity/полупрозрачность of active zoom + button is 0.5 means ZOOM is active
    # PLUS_ZOOMED_IN = (By.XPATH, "(//i[@class='ngi-icon-plus-simple-bold'])[2]")
    PIN = (By.XPATH, "//div[contains(@style,'position: absolute; left: 50%; top: 50%; width: 100%;')]//img[contains(@src, 'pin')]") # selenium size(e.size)/selenium location(e.location) tools for possible use
    # PIN =  (By.XPATH, "//div[contains(@style,position: absolute; left: 0px; top: 0px; user-select: none; width: 0px; height: 0px;')]//img[contains(@src, 'pin')]") # selenium size(e.size)/selenium location(e.location) tools for possible use
    # PIN = (By.XPATH, "(//img[@draggable='false'])[1]//img[contains(@src, 'pin')]")

    def search_port(self, port_name):
        self.input_text(port_name, *self.SEARCH_BAR)

    def click_top_search_result(self):
        self.wait_for_element_click(*self.FOUND_PORT_LIST_ITEM)

    def verify_map_zoomed_in(self):
        self.wait_for_element_appear(*self.PLUS_ZOOMED_IN)

    def verify_port_in_middle(self):
        # Locator contains PIN's style => position: absolute; left: 50%; top: 50%; width: 100%; to confirm its position
        self.wait_for_element_appear(*self.PIN)

    def verify_pin_port_of_departure(self):
        expected_substring = 'pin-port-of-departure'
        assert expected_substring in self.find_element(*self.PIN).get_attribute('src'), \
            f"Expected PIN to have '{expected_substring}' in its src."
