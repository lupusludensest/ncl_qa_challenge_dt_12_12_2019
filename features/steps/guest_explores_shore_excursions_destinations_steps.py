from behave import *


@when('I search for destination "{search_word}"')
def search_excursions(context, search_word):
    context.app.shore_excursions.search_destination(search_word)
    context.app.shore_excursions.click_find_excursions()


@then('Results are filtered by "{filter_text}"')
def verify_results_filtered(context, filter_text):
    context.app.shore_excursions.verify_results_filtered(filter_text)


@then('Filter By Ports are only belong to "{port_options}"')
def verify_port_filter(context, port_options):
    context.app.shore_excursions.verify_port_filter(port_options)