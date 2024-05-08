import requests
import jsonpath
import json
import pytest

a=12
@pytest.mark.smoke
def test_get_request():
    print("test_get_request")

@pytest.mark.smoke
def test_post_request():
    print("test_post_request")

@pytest.mark.smoke
@pytest.mark.skip
def test_post_request_file():
    print("test_post_request_file")

@pytest.mark.smoke
@pytest.mark.skipif(a>10, reason="value of a is greater than 10")
def test_delete_request():
    print("test_delete_request")

@pytest.mark.xfail
@pytest.mark.smoke
def test_post_request_fail():
    print("test_post_request_fail")

@pytest.mark.sanity
def test_put_request():
    print("test_put_request")

test_get_request()
test_post_request()
test_post_request_file()
test_delete_request
test_put_request
test_post_request_fail()