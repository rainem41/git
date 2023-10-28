class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says 'woof'!")

# Создание объектов класса
fido = Dog("Fido", "Labrador")
spot = Dog("Spot", "Golden Retriever")

# Вызов метода bark() для каждого объекта
fido.bark()
spot.bark()