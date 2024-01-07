import base_person

man = base_person.Person('Олег', 52, 179)
man.description_person()
warrior = base_person.Warrior('Конан', 32, 200)
print('Нового человека зовут ' + warrior.description_person())
