from behave import *
from logs import logs_file

log = logs_file.get_logs()

@given('we have facebook API')
def given_method(context):
    log.info("hi i m log")
    print("This is given method")

@when('we enter valid credential')
def when_valid_method(context):
    print("This is when method")
    assert 2 == 2, "this is wrong values"

@when('we enter invalid credential')
def when_invalid_method(context):
    print("This is when method")
    assert 2 == 4, "this is wrong values"

@then('user will log in')
def then_method(context):
    print("This is then method")

@then('correct profile opened')
def and_correct_method(context):
    print("This is and method")

@then('incorrect profile opened')
def and_incorrect_method(contex):
    print("This is and method")

