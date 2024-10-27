import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_index(client):
    """Test the index route."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Login' in response.data  # Check for a specific string in the response data
    assert b'username' in response.data  # Check if the username field exists in the login form

def test_login_success(client):
    """Test successful login."""
    response = client.post('/login', data={'username': 'admin', 'password': 'password123'})
    assert response.data == b'Login successful!'  # Adjust based on your actual success response

def test_login_failure(client):
    """Test failed login with invalid credentials."""
    response = client.post('/login', data={'username': 'invalid_user', 'password': 'wrong_password'})
    assert response.status_code == 302  # Assuming it redirects on failure
    # Optionally check for a flash message or redirection
