from behave import *
from time import sleep


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
    context.app.shore_excursions.verify_page_opened()


@when('Price range is filtered to {rng}')
def price_range_is(context, rng):
    context.app.shore_excursions.open_page('shore-excursions/search?sort=searchWeight&perPage=12&priceRange=0+3000')


@then("Only shore excursions within range {rng} are displayed")
def no_more_thirty_is_here(context, rng):
    assert 'priceRange=0+30' in context.driver.current_url
    context.app.shore_excursions.price_range_present(rng)