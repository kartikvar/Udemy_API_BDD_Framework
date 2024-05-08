from behave import *
import requests
import json


@given("Valid data is given")
def add_book_valid_data(context):
    context.URL = "https://restful-booker.herokuapp.com/booking"
    context.body = {
        "firstname": "Swap Nulla",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    context.header = {
        "Content-Type": "application/json"
    }


@when('Add Book API is triggered')
def step_impl(context):
    context.response = requests.post(context.URL, json=context.body, headers=context.header, verify=False)


@then('Book is added')
def step_impl(context):
    # assert response.status_code == 201
    context.bookingID = context.response.json()["bookingid"]
    print("ID is --> ", context.bookingID)
    print("First Name is --> ", context.response.json()["booking"]["firstname"])
    # assert context.response.json()["Msg"] == "successfully added"
