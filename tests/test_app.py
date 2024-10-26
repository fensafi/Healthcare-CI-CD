from app import app

def test_index():
    with app.test_client() as client:
        response = client.get('/')
        # Check that the response status code is 302, indicating a redirect
        assert response.status_code == 302
        # Check that the redirect location is /login
        assert response.headers['Location'].endswith('/login')
