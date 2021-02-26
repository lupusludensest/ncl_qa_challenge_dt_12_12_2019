from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class ShoreExcursions(Page):
    SEARCH = (By.ID, 'search_destinations_chosen')
    SEARCH_BAR = (By.CSS_SELECTOR, 'input.chosen-search-input')
    SEARCH_RESULT = (By.CSS_SELECTOR, 'li.active-result')
    FIND_EXCURSIONS = (By.CSS_SELECTOR, "button[type='submit']")

    PRICE_RANGE_PRESENT = (By.CSS_SELECTOR, 'span.legend-column.extremes')
    RESULTS_FILTER = (By.CSS_SELECTOR, 'div.filter-options a.items-link')
    PORT_FILTER = (By.CSS_SELECTOR, "a[title='Port']")
    PORTS = (By.CSS_SELECTOR, "#ports li")


    def search_destination(self, search_word: str):
        """
        :param search_word: Search word for destination
        """
        self.click(*self.SEARCH)
        self.input_text(search_word, *self.SEARCH_BAR)
        sleep(3)
        self.click(*self.SEARCH_RESULT)
        sleep(3)

    def click_find_excursions(self):
        self.wait_for_element_click(*self.FIND_EXCURSIONS)

    def price_range_present(self, rng):
        text_here = self.find_element(*self.PRICE_RANGE_PRESENT).text
        print(f'\nActual text: {text_here} VS expected text: {rng}')
        assert rng == text_here, f'Expected text {rng}, but got {text_here}'


    def verify_page_opened(self):
        assert 'shore-excursions/search' in self.driver.current_url, \
            f"Expected 'shore-excursions' page to open, but got {self.driver.current_url}"

    def verify_results_filtered(self, expected_filter_text):
        filter_text = self.find_element(*self.RESULTS_FILTER).text
        assert expected_filter_text == filter_text, \
            f"Expected text to be '{expected_filter_text}' but got '{filter_text}'"

    def verify_port_filter(self, port_options):
        # Get a list of expected port locations from the step
        expected_ports = port_options.split(', ')
        print(f'\nExpected ports: {expected_ports}')
        self.click(*self.PORT_FILTER)

        # Make sure port list has opened before verification
        self.wait_for_element_appear(*self.PORTS)

        ports = self.find_elements(*self.PORTS)
        # Verify each port destination belongs to expected ports
        for port in ports:
            actual_port_destination = port.text.split(', ')[1]
            print(f'\nActual port destiantion: {actual_port_destination}')
            assert actual_port_destination in expected_ports, \
                f"Actual {actual_port_destination} not in expected {expected_ports}"
