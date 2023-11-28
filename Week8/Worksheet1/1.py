import datetime


global ID
ID = 10*3


class Rental:
    def __init__(self):
        self.users = []
        self.vehicles = []
        self.available_vehicles = []
        self.logs = {}


class Vehicle:
    def __init__(self, manufacturer: str, model: str, year: int, daily_rental_rate: int):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.daily_rental_rate = daily_rental_rate

    def __str__(self):
        return f'{self.model} costs £{self.daily_rental_rate} per day'


class Car(Vehicle):
    def __init__(self, manufacturer: str, model: str, year: int, daily_rental_rate: int,
                 doors: int, seats: int, fuel: str):
        super().__init__(manufacturer, model, year, daily_rental_rate)
        self.doors_amount = doors
        self.seats_amount = seats
        self.fuel_type = fuel


class Truck(Vehicle):
    def __init__(self, manufacturer: str, model: str, year: int, daily_rental_rate: int, cargo: int, driver: str):
        super().__init__(manufacturer, model, year, daily_rental_rate)
        self.cargo_capacity = cargo
        self.driver_type = driver


class Motorcycle(Vehicle):
    def __init__(self, manufacturer: str, model: str, year: int, daily_rental_rate: int, engine: str, cylinders: int):
        super().__init__(manufacturer, model, year, daily_rental_rate)
        self.engine_displacement = engine
        self.cylinders_amount = cylinders


class Customer(Rental):
    def __init__(self, name: str, address: str, phone: int):
        # global ID
        self.name = name
        self.address = address
        self.phone_number = phone
        self.customer_ID = ID
        ID += 1


RentCompanySunrise = Rental()
mainloop = True
while mainloop:
    a = int(input('Type 0 if you want to exit\nType 1 if you want to see the information about available vehicles'
                  '\nType 2 if you want to calculate the cost of your rent\nType 3 if you want to rent the car'
                  '\nType 4 if you want to return a vehicle\nType 5 if you want to see logs'))
    if a == 0:
        mainloop = 0
    elif a == 1:
        print(RentCompanySunrise.available_vehicles)
    elif a == 2:
        car = input('Type model of the car you want to rent: ')
    elif a == 3:
        car = input('Type model of the car you want to rent: ')
    elif a == 4:
        user = input('Type your user ID')
    elif a == 5:
        print(RentCompanySunrise.logs)
