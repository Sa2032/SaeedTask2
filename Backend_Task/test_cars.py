import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app, fake_db
from unittest.mock import patch

client = TestClient(app)

@pytest.fixture
def clear_db():
    fake_db.clear()

def test_create_car(clear_db):
    car_data = {"id": 1, "make": "Toyota", "model": "Corolla", "year": 2020}
    response = client.post("/cars/", json=car_data)
    assert response.status_code == 200
    assert response.json() == car_data

def test_create_car_already_exists(clear_db):
    car_data = {"id": 1, "make": "Toyota", "model": "Corolla", "year": 2020}
    client.post("/cars/", json=car_data)
    response = client.post("/cars/", json=car_data)
    assert response.status_code == 400
    assert response.json() == {"detail": "Car already exists"}

def test_read_cars(clear_db):
    car_data = {"id": 1, "make": "Toyota", "model": "Corolla", "year": 2020}
    client.post("/cars/", json=car_data)
    response = client.get("/cars/")
    assert response.status_code == 200
    assert response.json() == [car_data]

def test_read_car(clear_db):
    car_data = {"id": 1, "make": "Toyota", "model": "Corolla", "year": 2020}
    client.post("/cars/", json=car_data)
    response = client.get("/cars/1")
    assert response.status_code == 200
    assert response.json() == car_data

def test_read_car_not_found(clear_db):
    response = client.get("/cars/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Car not found"}

def test_update_car(clear_db):
    car_data = {"id": 1, "make": "Toyota", "model": "Corolla", "year": 2020}
    client.post("/cars/", json=car_data)
    updated_car = {"id": 1, "make": "Toyota", "model": "Camry", "year": 2021}
    response = client.put("/cars/1", json=updated_car)
    assert response.status_code == 200
    assert response.json() == updated_car

def test_update_car_not_found(clear_db):
    updated_car = {"id": 999, "make": "Toyota", "model": "Camry", "year": 2021}
    response = client.put("/cars/999", json=updated_car)
    assert response.status_code == 404
    assert response.json() == {"detail": "Car not found"}

def test_delete_car(clear_db):
    car_data = {"id": 1, "make": "Toyota", "model": "Corolla", "year": 2020}
    client.post("/cars/", json=car_data)
    response = client.delete("/cars/1")
    assert response.status_code == 200
    assert response.json() == car_data

def test_delete_car_not_found(clear_db):
    response = client.delete("/cars/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Car not found"}

@patch("main.send_email")
def test_create_car_with_email(mock_send_email, clear_db):
    car_data = {"id": 1, "make": "Toyota", "model": "Corolla", "year": 2020}
    response = client.post("/cars/", json=car_data)
    assert response.status_code == 200
    assert response.json() == car_data
    mock_send_email.assert_called_once_with(car_data)

