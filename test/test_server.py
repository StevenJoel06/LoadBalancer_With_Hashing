import requests

def test_home():
    response = requests.get('http://localhost:5000/home')
    assert response.status_code == 200
    data = response.json()
    assert "Hello from Server" in data["message"]

def test_heartbeat():
    response = requests.get('http://localhost:5000/heartbeat')
    assert response.status