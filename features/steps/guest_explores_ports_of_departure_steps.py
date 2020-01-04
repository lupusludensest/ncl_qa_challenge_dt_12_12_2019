from behave import *
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

use_step_matcher("re")


@step('I navigated to "Shore Excursion" page')
def navigated_shore_excursions(context):
    context.app.top_navigation.click_explore()
    context.app.top_navigation.click_shore_excursions()


@step("I click Find Excursions")
def nav_excursions(context):
    context.app.shore_excursions.click_find_excursions()
    sleep(2)


@step("Shore Excursions page is present")
def shore_exc_is_present(context):
    context.app.shore_excursions.text_is_present()


@when('Price range is filtered to "\$0-\$30"')
def price_range_is(context):
    context.app.shore_excursions.price_range_present()


@then("Only shore excursions within range are displayed")
def no_more_thirty_is_here(context):
    context.app.shore_excursions.open_page('shore-excursions/search?sort=searchWeight&perPage=12&priceRange=0+30')
    assert 'priceRange=0+30' in context.driver.current_url




