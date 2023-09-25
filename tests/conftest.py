import pytest
from app import app

@pytest.fixture
def api():
    api = app.test_client()
    return api