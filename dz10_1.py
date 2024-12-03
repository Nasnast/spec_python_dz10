'''Задание 1. Отцы, матери и дети.
 Реализуйте два класса: «Родитель» и «Ребёнок». У родителя есть:
 ● имя,
 ● возраст,
 ● список детей.
 Ионможет:
 ● сообщить информацию о себе,
 ● успокоить ребёнка,
 ● покормить ребёнка.
 У ребёнка есть:
 ● имя,
 ● возраст (должен быть меньше возраста родителя хотя бы на 16 лет),
 ● состояние спокойствия,
 ● состояние голода.
 Реализация состояний — на ваше усмотрение. Это может быть и простой «флаг»,
 и словарь состояний, и что-то поинтереснее'''

class Parent:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.child = []

    def info_parent(self):
        return (f'меня зовут {self.name}, мне {self.age} лет.')

    def add_child(self, child):
        if self.age - child.age >= 16:
            self.child.append(child)
        else:
            print(f'{child.name} не ребенок {self.name}')

    def list_child(self):
        if self.child:
            print(f'Дети {self.name}: ')
            for child in self.child:
                print(f'{child.name}')
        else:
            print(f'у {self.name} нет детей')

    def get_hungry(self):
        for child in self.child:
            if child.hungry:
                print(f'{self.name} покормил {child.name}')
                child.hungry = False

    def get_calm(self):
        for child in self.child:
            if child.calm:
                print(f'{self.name} успокоил {child.name}')
                child.calm = False
            # else:
            #     print(f'{child.name} не ребенок {self.name}')


class Child:
    # hungry = True  # голодный
    # calm = True  # спокойный
    def __init__(self, name: str, age: int, hungry: bool, calm: bool):
        self.name = name
        self.age = age
        self.hungry = hungry
        self.calm = calm

    def child_status(self):
        hungry_status = 'голоден' if self.hungry else 'не голоден'
        calm_status = 'бесспокоен' if self.calm else 'спокоен'
        print(f'ребенок {self.name} {hungry_status} и {calm_status}')

    def __str__(self):
        """Представление объекта ребёнка в виде строки"""
        return (f'Ребенок {self.name}, {self.age} лет. {self.hungry} и {self.calm}')






if __name__ == '__main__':
    parent_1 = Parent('Sveta', 40)
    child_1 = Child('Masha', 30, True, True )
    child_2 = Child('Katya', 10, True, True)
    child_3 = Child('Vova', 5, True, True)
    parent_2 = Parent('Dima', 50)

    print(parent_1.info_parent())

    for child in [child_1, child_2, child_3]:
        parent_1.add_child(child)
        parent_2.add_child(child)

    parent_1.list_child()
    parent_2.list_child()

    child_2.child_status()
    child_3.child_status()

    for child in parent_1.child:
        parent_1.get_hungry()
        parent_1.get_calm()
        child.child_status()