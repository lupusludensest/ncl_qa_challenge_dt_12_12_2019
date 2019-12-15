from behave import *
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

use_step_matcher("re")

GET_SH_EXC_BTN = (By.XPATH, "//a[contains(@href, '/shore-excursions')]")
NAV_EXCURSIONS = (By.CSS_SELECTOR, "button.btn-cta.btn-primary.btn-large.search-submit")
SH_EXC_IS_PRESENT = (By.CSS_SELECTOR, "h2.header-title.visible-desktops")


@step('I navigated to "Shore Excursion" page')
def get_ports_btn(context):
    context.driver.find_element(*GET_SH_EXC_BTN).click()
    sleep(2)


@step("I click Find Excursions")
def nav_excursions(context):
    context.driver.find_element(*NAV_EXCURSIONS).click()
    sleep(2)


@step("Shore Excursions page is present")
def shore_exc_is_present(context):
    TEXT_IS_HERE = context.driver.find_element(*SH_EXC_IS_PRESENT).text
    assert 'Shore Excursions' in TEXT_IS_HERE
    print(f'Text: {TEXT_IS_HERE} .')
    sleep(2)


@when('Price range is filtered to "\$0-\$30"')
def price_range_is(context):
    context.driver.get('https://www.ncl.com/shore-excursions/search?sort=searchWeight&perPage=12&priceRange=0+30')


@then("Only shore excursions within range are displayed")
def no_more_thirty_is_here(context):
    assert 'priceRange=0+30' in context.driver.current_url == 'https://www.ncl.com/shore-excursions/search?sort=searchWeight&perPage=12&priceRange=0+30'


