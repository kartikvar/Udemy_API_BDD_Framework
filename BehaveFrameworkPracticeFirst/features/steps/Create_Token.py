from behave import *
import requests
from utilities.configurations import *
from utilities.resources import *

create_token_url = getConfig()["API"]["baseURL"] + APIResources.createToken
print("Create token url is -------------------------------------------------------->", create_token_url)

@given("Valid username and password is entered")
def enter_valid_data(context):
    context.data = {
        "username": "admin",
        "password": "password123"
    }

    context.header = {
        "Content-Type": "application/json"
    }

@when("Create Token API is triggered with valid data")
def create_token_api_is_triggered_with_valid_data(context):
    context.response_with_valid_data = requests.post(create_token_url, json=context.data, headers=context.header, verify=False)

@then("Token is created")
def token_is_created(context):
    print("Status code is --> ", context.response_with_valid_data.status_code)
    print("Asserting status code")
    assert context.response_with_valid_data.status_code == 200
    context.response_with_valid_data.json()

@given("Invalid {username} and {password} is entered")
def enter_invalid_data(context, username, password):

    context.data = {
        "username": username,
        "password": password
    }

    context.header = {
        "Content-Type": "application/json"
    }

@when("Create Token API is triggered with invalid data")
def create_token_api_is_triggered_with_invalid_data(context):
    context.response_with_invalid_data = requests.post(create_token_url, json=context.data, headers=context.header, verify=False)

@then("Token is not created")
def token_is_not_created(context):
    print("Checking if status code is not zero")
    assert context.response_with_invalid_data.status_code == 200
    reason = context.response_with_invalid_data.json()["reason"]
    print("reason is -------------------------> ", reason)