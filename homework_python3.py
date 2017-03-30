import random


class Car(object):
    def __init__(self, engine_count, tank_count):
        self.price = 10000.0
        self.car_credit = 0
        self.km = 100
        self._install_engine(engine_count)
        self._install_tank(tank_count)
        self.mileage = 0
        self.route = 0  # TODO move attribute to class Taxis
        self.isReady = True
        self.beenService = False

        # TODO create class with constant attributes

    def _set_new_engine(self, engine_type, consumption):
        # assert isinstance(engine_type, str)
        # assert isinstance(consumption, int)
        self.engine = Engine(engine_type, consumption)

    def _install_engine(self, engine_count):
        if engine_count != 3:
            self._set_new_engine("Petrol", 8)
        else:
            self._set_new_engine("Diesel", 6)

    def set_new_diesel(self):
        self._set_new_engine("Diesel", 6)

    def set_new_petrol(self):
        self._set_new_engine("Petrol", 8)

    def get_engine_type(self):
        return self.engine.fuel

    @classmethod
    def replace_engine(cls):
        if cls.get_engine_type == "Petrol":
            cls.car_credit += 3000
            return cls(engine=Engine(fuel="Petrol", consumption=8))
        else:
            cls.car_credit += 3000
            return cls(engine=Engine(fuel="Diesel", consumption=6))

    def _set_new_tank(self, volume):
        # assert isinstance(volume, str)
        self.tank = Tank(volume)

    def _install_tank(self, tank_count):
        if tank_count != 5:
            self._set_new_tank(volume=60)
        else:
            self._set_new_tank(volume=75)

    def check_fuel(self):
        if self.tank.actual_volume == 0:
            self.refuel()
        elif self.tank.actual_volume < (self.engine.consumption / 100):
            self.refuel()

    def refuel(self):
        volume_filling = (self.tank.volume - self.tank.actual_volume)
        self.tank.actual_volume += volume_filling
        self.tank.fuel_bill += self.engine.fuel_price * volume_filling * self.engine.amortization_ratio
        self.tank.count_refuelling += 1

    def check_mileage(self):
        if self.engine.fuel == "Petrol":
            if self.mileage >= 50000 and not self.engine.fuel_price == 2.4:
                self.engine.set_fuel_price(price=2.4)
            if self.mileage == 100000 and not self.beenService:
                self.isReady = False
                self.go_service()
        elif self.mileage == 150000 and self.engine.fuel == "Diesel" and not self.beenService:
            self.isReady = False
            self.go_service()

    def go_service(self):
        if self.engine.fuel == "Petrol":
            self.car_credit += 500
            self.isReady = True
            self.beenService = True
        elif self.engine.fuel == "Diesel":
            self.car_credit += 700
            self.isReady = True
            self.beenService = True

    '''def amortization(self):
        self.mileage += 1
        self.route -= 1
        self.engine.amortization_ratio = ((self.mileage / 1000) * 0.01) + 1
        if self.engine.fuel == "Petrol" and self.price_ratio != self.mileage / 1000:
            self.price -= (self.mileage / 1000) * 9.5
            self.price_ratio = self.mileage / 1000
        elif self.engine.fuel == "Diesel" and self.price_ratio != self.mileage / 1000:
            self.price -= (self.mileage / 1000) * 10.5
            self.price_ratio = self.mileage / 1000
        if self.price <= 0:
            self.isReady = False'''

    def amortization(self):
        self.mileage += 1
        self.route -= 1
        self.engine.amortization_ratio = ((self.mileage / 1000) * 0.01) + 1
        if self.engine.fuel == "Petrol" and self.mileage % 1000 == 0:
            self.price -= 9.5
        elif self.engine.fuel == "Diesel" and self.mileage % 1000 == 0:
            self.price -= 10.5
        if self.price <= 0:
            self.isReady = False

    def ride(self):
        self.tank.actual_volume -= self.engine.consumption / 100.0

    def get_price(self):
        return self.price

    '''#@property
    def mileage(self):
        return self.mileage'''

    '''#@mileage.setter
    def mileage(self, value):
        self._mileage = value'''


class Engine:
    def __init__(self, fuel, consumption):
        self.fuel_price = 0
        self.fuel = fuel
        self.consumption = consumption
        self.amortization_ratio = 1
        self.taxis_balance = 0
        self._init_fuel_price()

    def set_fuel_price(self, price):
        assert isinstance(price, float)
        self.fuel_price = price
        return self.fuel_price

    def _init_fuel_price(self):
        if self.fuel == "Petrol":
            self.fuel_price = 2.2
        else:
            self.fuel_price = 1.8

    def get_engine_consumption(self):
        return self.consumption


class Tank:
    def __init__(self, volume):
        self.volume = volume
        self.actual_volume = 0
        self.fuel_bill = 0
        self.count_refuelling = 0


class Taxis(object):
    def __init__(self):
        self.taxis_balance = 0
        self.cars_list = []
        self.petrol_cars = []
        self.diesel_cars = []
        self.car_producer(100)
        self.get_routes()

    def car_producer(self, capacity):
        e_count = 0
        t_count = 0
        for _ in xrange(capacity):
            car = Car(e_count, t_count)
            self.cars_list.append(car)

            if e_count != 3:
                e_count += 1
            else:
                e_count = 0

            if t_count != 5:
                t_count += 1
            else:
                t_count = 0

    @staticmethod
    def prepare_trip(car):
        car.check_mileage()
        car.check_fuel()

    def get_routes(self):
        for car in self.cars_list:
            car.route = random.randint(55000, 286000)

    def get_status(self):
        self.sort()
        print('--------List of Petrol cars--------')
        self.print_car_list(self.petrol_cars)
        print('--------List of Diesel cars--------')
        self.print_car_list(self.diesel_cars)
        self.sum_balance()

    def print_car_list(self, lst):
        for car in lst:
            print(
                "This car contains {} engine. Mileage is {}. Car price is {}. Total fuel bill is {} and {} times was at the gas station.".format(
                    car.engine.fuel, car.mileage, car.price, car.tank.fuel_bill, car.tank.count_refuelling))

    def sum_balance(self):
        for car in self.cars_list:
            self.taxis_balance += car.price - car.tank.fuel_bill - car.car_credit
        print("Taxis summary balance is {}".format(self.taxis_balance))

    def get_trips(self):
        for car in self.cars_list:
            while car.route and car.isReady:
                self.prepare_trip(car)
                car.ride()
                car.amortization()

    def sort(self):
        self.petrol_cars = [car for car in self.cars_list if car.engine.fuel == 'Petrol']
        self.petrol_cars = sorted(self.petrol_cars, key=lambda petrol_car: petrol_car.mileage)
        self.diesel_cars = [car for car in self.cars_list if car.engine.fuel == 'Diesel']
        self.diesel_cars = sorted(self.diesel_cars, key=lambda diesel_car: -diesel_car.price)


t = Taxis()
t.get_trips()
t.get_status()
