import requests

def test_get_replicas():
    response = requests.get('http://localhost:5000/rep')
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "successful"

def test_add_server():
    payload = {"n": 1, "hostnames": ["Server4"]}
    response = requests.post('http://localhost:5000/add', json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "successful"

def test_remove_server():
    payload = {"n": 1, "hostnames": ["Server4"]}
    response = requests.delete('http://localhost:5000/rm', json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "successful"