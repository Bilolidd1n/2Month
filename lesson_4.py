
class Fish:
    def __init__(self, name, color, size, speed):
        self.name = name
        self.color = color
        self.size = size
        self.speed = speed
        self.hunger = True

    def swim(self):
        print(f'{self.name} плывет со скоростью {self.speed}')
        
    def feed(self):
        self.hunger = False
        print(f"{self.name} накормлена!")

    def hunger(self):
        if self.hunger:
            print(f"{self.name} голодна!")
        else:
            print(f"{self.name} сыта!")

class GoldFish(Fish):
    def __init__(self, name):
        super().__init__(name, color='Золотой', size='Небольшая', speed='Медленная')

class Shark(Fish):
    def __init__(self, name):
        super().__init__(name, color='Серый', size='Крупная', speed='Быстрая')

class ClownFish(Fish):
    def __init__(self, name):
        super().__init__(name, color='Оранжевый с белыми полосами', size='Средняя', speed='Средняя')

class Aquarium:
    def __init__(self):
        self.fish_list = []

    def add_fish(self, fish):
        self.fish_list.append(fish)
        print(f"{fish.name} добавлена в аквариум")

    def remove_fish(self, fish):
        if fish in self.fish_list:
            self.fish_list.remove(fish)
            print(f"{fish.name} удалена из аквариума")
        else:
            print(f"{fish.name} не найдена в аквариуме")

    def watch(self):
        if not self.fish_list:
            print("В аквариуме нет рыбок")
        else:
            for fish in self.fish_list:
                fish.swim()

    def feed(self):
        print("Рыбки накормлены")
        for fish in self.fish_list:
            fish.feed()

    def hunger(self):
        for fish in self.fish_list:
            fish.hunger()

aquarium = Aquarium()
goldfish = GoldFish('Содик Рыбка')
shark = Shark('Акула')
clownfish = ClownFish('Рыба клоун')
aquarium.add_fish(goldfish)
aquarium.add_fish(shark)
aquarium.add_fish(clownfish)
aquarium.watch()
aquarium.feed()
aquarium.watch()
aquarium.remove_fish(goldfish)

# Задание: Создание виртуального аквариума

# Представьте, что вам нужно смоделировать работу виртуального аквариума с рыбками.

# Создайте класс Fish:

# У каждой рыбки есть имя, цвет, размер и скорость плавания.
# Добавьте метод swim(), который выводит сообщение, например, "<имя рыбки> плывет со скоростью <скорость>".
# Создайте несколько классов рыбок:

# Goldfish (Золотая рыбка) – небольшая, медленная.
# Shark (Акула) – крупная, быстрая.
# Clownfish (Рыбка-клоун) – среднего размера, имеет яркий цвет и среднюю скорость.
# Создайте класс Aquarium, который будет содержать рыбок:

# Реализуйте методы для добавления и удаления рыбок из аквариума.
# Добавьте метод watch(), который выводит список всех рыбок в аквариуме и их действия (например, все рыбки плавают одновременно).
# Дополнительные детали:

# Сделайте метод feed() для класса Aquarium, который будет выводить сообщение о том, что рыбки накормлены.
# Добавьте свойство hunger для рыбок, которое увеличивается со временем, и обнуляется, когда рыбки накормлены.

