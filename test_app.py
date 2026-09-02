import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Logistica Andina Huancayo" in response.data

def test_inventario(client):
    response = client.get('/inventario')
    assert response.status_code == 200
    assert b"Laptop Corporativa" in response.data
