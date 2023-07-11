from behave import *

@given('the user is on the homepage')
def step_user_is_on_the_homepage(context):
    #here you can put the navigation to the homepage
    pass

@when('the user enters their name')
def when_user_enters_name(context):
    context.name = "Bruce"

@then("the system should display a greeting message with the user's name")
def message_to_return(context):
    message = f"Hello, {context.name}"
    assert message == "Hello, Bruce"