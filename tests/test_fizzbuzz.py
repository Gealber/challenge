import pytest


def test_fizzbuzz(client, fizzbuzz):
    assert client.get('/fizzbuzz').status_code == 400
    assert client.get('/fizzbuzz?start=1&nd=100').status_code == 400    
    assert client.get('/fizzbuzz?start=1&end=100').status_code == 200    
