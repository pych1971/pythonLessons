from base_person import Person


class Warrior(Person):
    """Создаём класс воина"""

    def __init__(self, name, age, height):
        super().__init__(name, age, height)
        self.rage = 100

    def get_rage(self):
        """Получение заряда ярости"""
        print('Заряд ярости равен', str(self.weight))

    def description_person(self):
        """Переопределение метода родителя"""
        description = self.name + ', ему ' + str(self.age) + ', его заряд ярости ' + str(self.rage)
        # print('Нового человека зовут', description)
        return description
