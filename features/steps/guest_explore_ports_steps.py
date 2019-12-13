from behave import given, when, then


@given('I am on Homepage')
def open_homepage(context):
    context.app.page.open_page()


@given('I navigated to "Ports" page')
def navigate_ports(context):
    context.app.top_navigation.click_explore()
    context.app.top_navigation.click_ports()


@when('I search for "{port_city}" port')
def search_port(context, port_city):
    context.app.port_of_call_page.search_port(port_city)
    context.app.port_of_call_page.click_top_search_result()


@then('Map zoomed to show selected port')
def verify_map_zoomed(context):
    context.app.port_of_call_page.verify_map_zoomed_in()


@then('Port is on the middle of the map')
def verify_port_in_middle(context):
    context.app.port_of_call_page.verify_port_in_middle()


@then('Port displayed as "Port Of Departure"')
def verify_pin_port_of_departure(context):
    context.app.port_of_call_page.verify_pin_port_of_departure()
