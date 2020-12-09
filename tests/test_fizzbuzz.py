import pytest


def test_fizzbuzz(client, fizzbuzz):
    assert client.get('/fizzbuzz').status_code == 405
    assert fizzbuzz.result().status_code == 200
