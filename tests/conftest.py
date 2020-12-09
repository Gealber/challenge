import pytest
import os
import tempfile
from challenge import create_app

@pytest.fixture
def app():
    app = create_app({
        'TESTING': True,
    })

    yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()


class FizzBuzz(object):
    def __init__(self, client):
        self._client = client
    
    def result(self, start=1, end=100):
        return self._client.post(
            '/fizzbuzz',
            data={'start': start, 'end': end}
        )

@pytest.fixture
def fizzbuzz(client):
    return FizzBuzz(client)