from behave import *
import requests


@given('Valid GitHub credentials')
def step_impl(context):
    context.se = requests.session()
    context.se.auth = auth = ("kartikvar@gmail.com", "Mygithubpassword@2")
    context.URL = "https://api.github.com/user/repos"


@when('Get Repo API is triggered')
def step_impl(context):
    context.response = context.se.get(context.URL, verify=False)


@then('Status code is 200')
def step_impl(context):
    assert context.response.status_code == 200