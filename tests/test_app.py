from app import app

def test_index():
    with app.test_client() as client:
        response = client.get('/')
        print(f'Response Status Code: {response.status_code}')
        print(f'Response Data: {response.data}')
        assert response.status_code == 200  # Update this line

