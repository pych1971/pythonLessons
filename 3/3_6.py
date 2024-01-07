class Car():
    """Создаём автомобиль"""

    def __init__(self, model, year, capacity, price, mileage):
        """Создаём атрибуты автомобиля"""
        self.model = model
        self.year = year
        self.capacity = capacity
        self.price = price
        self.mileage = mileage
        self.wheels = 4

    def description_car(self):
        """Получение описания автомобиля"""

        description = f'Модель {self.model} {self.year} года. Объём двигателя - {self.capacity} л, цена - ${self.price}, пробег - {self.mileage} км, {self.wheels} колеса.'
        print(description)


class Truck(Car):
    """Создаём класс Грузовик"""

    def __init__(self, model, year, capacity, price, mileage):
        super().__init__(model, year, capacity, price, mileage)
        self.wheels = 8


car = Car('Jaguar', 2023, 63, 40000, 30000)
car.description_car()
truck = Truck('Scania', 2023, 500, 150000, 60000)
truck.description_car()
