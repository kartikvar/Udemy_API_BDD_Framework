import requests


def before_all(context):
    print("This is before all")


def before_feature(context, feature):
    print("This is before feature")


def before_scenario(context, scenario):
    print("This is before scenario")


def before_step(context, step):
    print("This is before step")


def after_step(context, step):
    print("This is after step")


def after_scenario(context, scenario):
    if "environment" in scenario.tags:
        URI = "https://restful-booker.herokuapp.com/booking/"
        endPoint = str(context.bookingID)
        URL = URI + endPoint
        response = requests.get(URL, verify=False)
        print("First Name in after scenario is --> ", response.json()["firstname"])



def after_feature(context, feature):
    print("This is after feature")


def after_all(context):
    print("This is after all")
