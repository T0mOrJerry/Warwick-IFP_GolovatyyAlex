import datetime
from math import pi


class Rental:
    def __init__(self):
        self.customers = []
        self.vehicles = []
        self.available_vehicles = []
        self.vehicles_model = {}
        self.customer_id = {}
        self.customer_rent = {}
        self.logs = []

    def add_customer(self, cust):
        self.customers.append(cust)
        self.customer_id[cust.customer_id] = cust
        self.customer_rent[cust.customer_id] = []
        log = {'type': 'Customer adding', 'data': datetime.date.today()}
        self.logs.append(log)

    def add_vehicle(self, veh):
        self.vehicles.append(veh)
        self.available_vehicles.append(veh)
        self.vehicles_model[veh.model] = veh
        log = {'type': 'Vehicle adding', 'data': datetime.date.today()}
        self.logs.append(log)

    def rent(self, car_name, cust):
        vehi = self.vehicles_model[car_name]
        if vehi not in self.available_vehicles:
            return 'All vehicles of this model are booked'
        self.available_vehicles.pop(self.available_vehicles.index(vehi))
        self.customer_rent[int(cust)].append(vehi)
        log = {'type': 'Vehicle rent', 'user': int(cust), 'vehicle': vehi.model, 'date': datetime.date.today()}
        self.logs.append(log)
        return 'Success'

    def returning(self, car_name, cust):
        vehi = self.vehicles_model[car_name]
        if vehi not in self.customer_rent[int(cust)]:
            return "You haven't rented this car"
        self.available_vehicles.append(vehi)
        self.customer_rent[int(cust)].pop(self.customer_rent[int(cust)].index(vehi))
        log = {'type': 'Vehicle return', 'user': int(cust), 'vehicle': vehi.model, 'date': datetime.date.today()}
        self.logs.append(log)
        return 'Success'

    def calculate(self, car_name, day):
        vehi = self.vehicles_model[car_name]
        return f'Rent of this vehicle for {day} days costs £{vehi.daily_rental_rate * int(day)}'


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
    def __init__(self, name: str, address: str, phone: str, id: int, staff: bool):
        self.name = name
        self.address = address
        self.phone_number = phone
        self.customer_id = id
        self.staff = staff


RentCompanySunrise = Rental()
RentCompanySunrise.add_customer(Customer('Alex', 'Gibbet Hill Road', '07401123456', 1000, True))
RentCompanySunrise.add_customer(Customer('Not Alex', 'God Knows Where Road', '07401654321', 1001, False))
RentCompanySunrise.add_vehicle(Car('NOIDEA', 'AAAA1', 2077, 64, 2.5, pi, "Elves' blood"))
RentCompanySunrise.add_vehicle(Car('NOIDEA', 'BYOB', 1825, 3, 5, 43, "Dark side of the force"))
RentCompanySunrise.add_vehicle(Motorcycle('BLYAEB', 'T1000', 2022, 700, 'Magical', 1))
mainloop = True
while mainloop:
    a = int(input('Type 0 if you want to exit\nType 1 if you want to see the information about available vehicles'
                  '\nType 2 if you want to calculate the cost of your rent\nType 3 if you want to rent the car'
                  '\nType 4 if you want to return a vehicle\nType 5 if you want to see logs\n'))
    if a == 0:
        mainloop = 0
    elif a == 1:
        print(list(map(str, RentCompanySunrise.available_vehicles)))
    elif a == 2:
        car = input('Type model of the vehicle you want to rent: ')
        if car in RentCompanySunrise.vehicles_model:
            days = input('For how much days do you want to take the vehicle: ')
            print(RentCompanySunrise.calculate(car, days))
        else:
            print("We don't have this vehicle")
    elif a == 3:
        user = int(input('Type your customer_id: '))
        if user in RentCompanySunrise.customer_id:
            car = input('Type model of the vehicle you want to rent: ')
            if car in RentCompanySunrise.vehicles_model:
                print(RentCompanySunrise.rent(car, user))
            else:
                print("We don't have this vehicle")
        else:
            print("There is no such user")
    elif a == 4:
        user = int(input('Type your customer_id: '))
        if user in RentCompanySunrise.customer_id:
            car = input('Type model of the vehicle you want to return: ')
            if car in RentCompanySunrise.vehicles_model:
                print(RentCompanySunrise.returning(car, user))
            else:
                print("We don't have this vehicle")
        else:
            print("There is no such user")
    elif a == 5:
        print(RentCompanySunrise.logs)
    print()
