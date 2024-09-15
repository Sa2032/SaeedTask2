from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional
import requests

app = FastAPI()

class Car(BaseModel):
    id: int
    make: str
    model: str
    year: int

fake_db = {}

@app.post("/cars/", response_model=Car)
def create_car(car: Car):
    if car.id in fake_db:
        raise HTTPException(status_code=400, detail="Car already exists")
    fake_db[car.id] = car
    return car

@app.get("/cars/", response_model=List[Car])
def read_cars():
    return list(fake_db.values())

@app.get("/cars/{car_id}", response_model=Car)
def read_car(car_id: int):
    car = fake_db.get(car_id)
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    return car

@app.put("/cars/{car_id}", response_model=Car)
def update_car(car_id: int, car: Car):
    if car_id not in fake_db:
        raise HTTPException(status_code=404, detail="Car not found")
    fake_db[car_id] = car
    return car

@app.delete("/cars/{car_id}", response_model=Car)
def delete_car(car_id: int):
    car = fake_db.pop(car_id, None)
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    return car


def send_email(car):
    response = requests.post("https://email-service.com/send", json={"car": car})
    return response

@app.post("/cars/", response_model=Car)
def create_car(car: Car):
    if car.id in fake_db:
        raise HTTPException(status_code=400, detail="Car already exists")
    fake_db[car.id] = car
    send_email(car)  
    return car


