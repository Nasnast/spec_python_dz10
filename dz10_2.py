'''Задача 2. Совместное проживание
 Чтобы понять, стоит ли ему жить с кем-то или лучше остаться в гордом
 одиночестве, Артём решил провести необычное исследование. Для этого он
 реализовал модель человека и модель дома.
 Человек может (должны быть такие методы):
 ● есть(+ сытость, − еда);
 ● работать (− сытость, + деньги);
 ● играть (− сытость);
 ● ходить в магазин за едой (+ еда, − деньги);
 ● прожить один день (выбирает одно действие согласно описанному ниже
 приоритету и выполняет его).
 У человека есть (должны быть такие атрибуты):
 ● имя,
 ● степень сытости (изначально 50),
 ● дом.
 В доме есть:
 ● холодильник с едой (изначально 50 еды),
 ● тумбочка с деньгами (изначально 0 денег).
 Если сытость человека становится меньше нуля, человек умирает.
 Логика действий человека определяется следующим образом:
1. Генерируется число кубика от 1 до 6.
 2. Если сытость < 20, то нужно поесть.
 3. Иначе, если еды в доме < 10, то сходить в магазин.
 4. Иначе, если денег в доме < 50, то работать.
 5. Иначе, если кубик равен 1, то работать.
 6. Иначе, если кубик равен 2, то поесть.
 7. Иначе играть.
 По такой логике эксперимента человеку надо прожить 365 дней.
 Реализуйте такую программу и создайте двух людей, живущих в одном доме.
 Проверьте работу программы несколько раз'''

from random import randint

class Human():
    def __init__(self, name, home):
        self.name = name
        self.hunger = 50 #ачальная сытость
        self.home = home #дом


    def eat_food(self):
        """Метод есть - увеличение сытости, уменьшение еды"""
        if self.home.food >= 10:
            self.hunger += 10
            self.home.food -= 10
            print(f'{self.name} поел. Сытость - {self.hunger}, количество еды - {self.home.food}')
        else:
            print(f'в холодильнике недостаточно еды')

    def work(self):
        """Метод работа - увеличение денег, уменьшение сытости"""
        self.hunger -= 10
        self.home.work_salary(50)
        print(f'{self.name} сегодня работал. Сытость уменьшилась до {self.hunger}, количество денег - {self.home.money}')

    def play(self):
        """Игра - уменьшает сытость"""
        self.hunger -= 10
        print(f'{self.name} поиграл, что уменьшило сытость до {self.hunger}')

    def shop_food(self):
        """Метод, который покупает еду за деньги"""
        self.home.buy_food(20, 50)

    def live_day(self):
        """Моделирование одного дня"""
        number = randint(1, 6)
        print(f'Сегодня число кубика {number}')

        if self.hunger <= 20:
            self.eat_food()
        elif self.home.food < 10:
            self.shop_food()
        elif self.home.money < 50:
            self.work()
        elif number == 1:
            self.work()
        elif number == 2:
            self.eat_food()
        else:
            self.play()

        if self.hunger <= 0:
            print(f'{self.name} умер от голода')
            return False
        return True


class Home:
    def __init__(self,  food= 50, money=0):
        self.food = food
        self.money = money

    def buy_food(self, quantity, price):
        """покупка еды"""
        if self.money >= price:
            self.money -= price
            self.food += quantity
            print(f'купили {quantity} единиц еды за {price} денег')

        else:
            print(f'недостаточно денег для покупки еды')

    def work_salary(self, salary):
        """плата за работу - увеличиваем количество денег """
        self.money += salary
        print(f'заработали {salary} денег')

if __name__ == '__main__':
    home1 = Home()
    home2 = Home()

    human1 = Human('Ivan', home1)
    human2 = Human('Sveta', home1)
    human3 = Human('Olya', home2)

    try:
        for day in range(1, 366): # 365 дней
            print(f'\n Day {day}')

            if not human1.live_day() or not human2.live_day() or not human3.live_day():
                print(f'человек умер на {day}')
                break
    finally:

        print(f'Итоги: ')
        print(f'Состояние пары: количество денег {home1.money}, количество еды {home1.food}')
        print(f'Одиночка: количество денег {home2.money}, количество еды {home2.food}')




