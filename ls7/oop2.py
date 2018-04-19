# есть класс "собака"
class Dog:
    name = ""


# есть класс "человек"
class Human:
    # у каждого человека по умолчанию есть собака
    # (конструктор автоматически присваивает человеку некую собаку)
    def __init__(self, dog):
        self.dog = dog

    # человек может дать собаке имя
    def name_the_dog(self):
        self.dog.name = "Jack"
        print(self.dog.name)


goodBoy = Dog()  # создаем объект "собака"
bill = Human(goodBoy)  # создаем объект "человек"

dogsName = bill.name_the_dog()  # просим человека дать собаке имя