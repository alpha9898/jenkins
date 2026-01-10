import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_status_code(client):
    """Test that home page returns 200 OK"""
    response = client.get('/')
    assert response.status_code == 200

def test_home_content(client):
    """Test that home page returns expected message"""
    response = client.get('/')
    assert b"Jenkins CI Pipeline is working!" in response.data

