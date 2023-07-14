from behave import *


@given('the user is on the dashboard')
def step_user_is_on_the_dashboard(context):
    pass

@when('the user clicks the logout button')
def step_when_user_clicks_logout_button(context):
    pass

@then('the system should display a logout message')
def step_message_to_return(context):
    print('You have successfully been logged out')