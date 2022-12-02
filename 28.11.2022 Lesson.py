class House():
    """Описание и чертеж домов"""
    def __init__(self, street, number, floor):
        self.street = street
        self.number = number
        self.floor = floor
        self.age = 0

    def check_build(self):
        print("Дом", self.number, "на улице", self.street, "уже достроен")


House1 = House("Moskow", 20, 9)
House2 = House("Toktogul", 18, 12)

print(House1.check_build())


class Human():
    """Описание человека"""
    def __init__(self, name, lastname, age, height, weight):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.height = height
        self.weight = weight

    def check_age(self):
        if self.age >= 21:
            print(self.name, "can enter in the club")
        else:
            print(self.name, "cannot enter in the club")

    def check_weight(self):
        if self.weight < 60:
            print(self.name, "you in the 1 weight group")
        else:
            print(self.name, "you in the 2 weight group")


def check_input_age(self, year):
    print(self.name, "age is", 2022 - year)


Person1 = Human("Daiana", "Rinat", 16, 173, 55)
Person2 = Human("Beks", "Maratov", 26, 178, 68)

print(Person1.check_age())
print(Person2.check_age())
print(Person1.check_weight())
print(Person2.check_weight())


class Human():
    """Описание человека"""
    def __init__(self, name, lastname, age, height, weight):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.height = height
        self.weight = weight

    def check_age(self):
        if self.age >= 21:
            print(self.name, "can enter in the club")
        else:
            print(self.name, "cannot enter in the club")

    def check_weight(self):
        if self.weight < 60:
            print(self.name, "you in the 1 weight group")
        else:
            print(self.name, "you in the 2 weight group")


def check_input_age(self, year):
    print(self.name, "age is", 2022 - year)


Person1 = Human("Daiana", "Rinat", 16, 173, 55)
Person2 = Human("Beks", "Maratov", 26, 178, 68)

print(Person1.check_age())
print(Person2.check_age())
print(Person1.check_weight())
print(Person2.check_weight())