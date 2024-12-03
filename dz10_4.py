''' Задача 4. Создание класса-фабрики для животных
 Создайте базовый класс Animal, который имеет атрибут name, представляющий имя
 животного.
 Создайте классы Bird, Fish и Mammal, которые наследуются от базового класса Animal и
 добавляют дополнительные атрибуты и методы:
 Bird имеет атрибут wingspan (размах крыльев) и метод wing_length, который
 возвращает длину крыла птицы.
 Fish имеет атрибут max_depth (максимальная глубина обитания) и метод depth, который
 возвращает категорию глубины рыбы (мелководная, средневодная, глубоководная) в
 зависимости от значения max_depth.
 Если максимальная глубина обитания рыбы (max_depth) меньше 10, то она относится к
 категории "Мелководная рыба".
 Если максимальная глубина обитания рыбы больше 100, то она относится к категории
 "Глубоководная рыба".
 В противном случае, рыба относится к категории "Средневодная рыба".
 Mammal имеет атрибут weight (вес) и метод category, который возвращает категорию
 млекопитающего (Малявка, Обычный, Гигант) в зависимости от веса. Если вес объекта
 меньше 1, то он относится к категории "Малявка".
 Если вес объекта больше 200, то он относится к категории "Гигант".
 В противном случае, объект относится к категории "Обычный".
 Создайте класс-фабрику AnimalFactory, который будет создавать экземпляры животных
 разных типов на основе переданного типа и параметров. Класс-фабрика должен иметь
 метод create_animal, который принимает следующие аргументы:
 animal_type (строка)- тип животного (один из: 'Bird', 'Fish', 'Mammal').
 *args- переменное количество аргументов, представляющих параметры для конкретного
 типа животного. Количество и типы аргументов могут различаться в зависимости от типа
 животного.
 Метод create_animal должен создавать и возвращать экземпляр животного заданного
 типа с переданными параметрами.
Если animal_type не соответствует 'Bird', 'Fish' или 'Mammal', функция вызовет ValueError с
 сообщением 'Недопустимый тип животного'''

class Animal:
    def __init__(self, name):
        self.name = name

class Bird(Animal):
    def __init__(self, name, weight, wingspan, color): # имя, вес, размах крыла, цвет
        super().__init__(name)
        self.weight = weight
        self.wingspan = wingspan
        self.color = color

    def wing_length(self): # длина крыла
        return self.wingspan / 2

    def __str__(self):
        return (f'Птичка - {self.name}, размах крыла - {self.wingspan}, длина крыла - {self.wing_length()}, цвет - {self.color}')

class Fish(Animal):
    def __init__(self, name, weight, depth, color): # макс глубина
        super().__init__(name)
        self.weight = weight
        self.color = color
        self.depth = depth

    def max_depth(self):
        if self.depth < 10:
            return f'мелководная рыба'
        elif self.depth < 100:
            return f'глубоководная рыба'

        return f'средневодная рыба'

    def __str__(self):
        return (f'Рыба - {self.name}, относится к типу - {self.max_depth()}, максимальная глубина - {self.depth}, цвет - {self.color}')

class Mammal(Animal):
    def __init__(self, name, weight, height, color):
        super().__init__(name)
        self.weight = weight
        self.height = height
        self.color = color

    def category(self):
        if self.weight < 1:
            return f'малявка'
        elif self.height > 200:
            return f'гигант'
        return f'обычный'

    def __str__(self):
        return (f'Млекопитающее - {self.name}, относится к типу - {self.category()}, вес - {self.weight}, цвет - {self.color}')

class AnimalFactory:
    def create_animal(animal_type: str, *args) -> Animal:
        '''создает экземпляр животного на основе переданного типа и параметров'''
        animal_classes = {'Bird': Bird,'Fish': Fish,'Mammal': Mammal}
        if animal_type in animal_classes:
            return animal_classes[animal_type](*args)
        else:
            raise ValueError(f'Неизвестный тип: {animal_type}')

    def __str__(self):
        return (self.factory)


if __name__ == '__main__':
    # factory = AnimalFactory()
    # factory.create_animal()
    # print(factory.__str__())
    bird1 = AnimalFactory.create_animal('Bird', 'pinguin', 10, 20, 'blue')
    print(bird1)
    print(f'Длина крыла {bird1.name} - {bird1.wing_length()} ')

    fish_clown = AnimalFactory.create_animal('Fish', 'clown', 1, 1, 'pink')
    print(fish_clown)
    print(f'{fish_clown.max_depth() = }')
    mammal_zebra = AnimalFactory.create_animal('Mammal', 'zebra', 100, 90, 'blue')
    print(mammal_zebra)
    print(f'{mammal_zebra.category() =}')


