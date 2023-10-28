class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says 'woof'!")

# Создание объектов класса
fido = Dog("Bobi", "Labrador")
spot = Dog("Toti", "Golden Retriever")

# Вызов метода bark() для каждого объекта
fido.bark()
spot.bark()