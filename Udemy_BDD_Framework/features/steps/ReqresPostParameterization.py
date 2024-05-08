from behave import *
import requests


@given('Valid user data is given')
def valid_data_given(context):
    context.URL = "https://reqres.in/api/users"
    context.body = {
        "name": "Kartik",
        "job": "Boss"
    }


@given('Valid {name} and {job} are given')
def valid_multiple_data_given(context, name, job):
    context.URL = "https://reqres.in/api/users"
    context.body = {
        "name": name,
        "job": job
    }


@when('Create user API is triggered')
def create_token_api_is_triggered(context):
    context.response = requests.post(context.URL, data=context.body, verify=False)


@then('Users are created')
def multiple_users_are_created(context):
    name = context.response.json()["name"]
    print("Name which is created is --> ", name)

@then('User is created')
def user_is_created(context):
    name = context.response.json()["name"]
    print("Name which is created is --> ", name)