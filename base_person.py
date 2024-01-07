class Person():
    """Создаём человека"""

    def __init__(self, name, age, height):
        """Инициализируем атрибуты человека"""
        self.name = name
        self.age = age
        self.height = height
        self.weight = 80

    def description_person(self):
        """Получение описания человека"""
        description = self.name + ', ему ' + str(self.age) + ', его рост ' + str(self.height) + ', его вес ' + str(
            self.weight)
        print('Нового человека зовут', description)

    def get_weight(self):
        """Получение веса человека"""
        print('Вес нашего человека -', str(self.weight))

    def update_weight(self, kg):
        """Изменение веса человека"""
        self.weight = kg
