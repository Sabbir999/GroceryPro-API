import os
from unittest import mock


def mock_env_variables(**envvars):
    """
    Decorator to mock the environment variables for the duration of the test.
    """
    return mock.patch.dict(os.environ, envvars)


class MockResponse:

    def __init__(self, status_code: int, body: dict):
        self.status_code = status_code
        self.body = body

    def json(self):
        return self.body
 