'''Задача3.Крестики-нолики
Создайте программу, которая реализует игру «Крестики-нолики».
 Для этого напишите:
 1. Класс, который будет описывать поле игры.
 class Board:
 # Класс поля, который создаёт у себя экземпляры клетки.
 # Пусть класс хранит информацию о состоянии поля (это может быть список из
 девяти элементов).
 # Помимо этого, класс должен содержать методы:
 # «Изменить состояние клетки». Метод получает номер клетки и, если клетка не
 занята, меняет её состояние. Если состояние удалось изменить, метод возвращает
 True, иначе возвращается False.
 # «Проверить окончание игры». Метод не получает входящих данных, но
 возвращает True/False. True — если один из игроков победил, False — если
 победителя нет.
 2. Класс, который будет описывать одну клетку поля:
 class Cell:
 # Клетка, у которой есть значения:
 # занята она или нет;
 # номер клетки;
 # символ, который клетка хранит (пустая, крестик, нолик).
 3. Класс, который описывает поведение игрока:
 class Player:
 # Уигрока может быть:
 # имя,
 # количество побед.
 # Класс должен содержать метод:
 # «Сделать ход». Метод ничего не принимает и возвращает ход игрока (номер
 клетки). Введённый номер нужно обязательно проверить.
 4. Класс, который управляет ходом игры:
class Game:
 # класс «Игры» содержит атрибуты:
 # состояние игры,
 # игроки,
 # поле.
 # Атакже методы:
 # Метод запуска одного хода игры. Получает одного из игроков, запрашивает у
 игрока номер клетки, изменяет поле, проверяет, выиграл ли игрок. Если игрок победил,
 возвращает True, иначе False.
 # Метод запуска одной игры. Очищает поле, запускает цикл с игрой, который
 завершается победой одного из игроков или ничьей. Если игра завершена, метод
 возвращает True, иначе False.
 # Основной метод запуска игр. В цикле запускает игры, запрашивая после каждой
 игры, хотят ли игроки продолжать играть. После каждой игры выводится текущий счёт
 игроков.'''

from random import randint

class Cell:
    def __init__(self, number):
        self.number = number
        self.occupied = False # Статус занятости клетки

class Board:
    def __init__(self):
        self.cells = [Cell(i) for i in range(1, 10)] # создаем 9 клеток для доски

    def display_board(self):
        """Игровое поле"""
        print("-" * 13)
        for i in range(3):
            print(f'| {self.cells[0 + i * 3].number} | {self.cells[1 + i * 3].number} | {self.cells[2 + i * 3].number} |')
            print("-" * 13)

    def check_win(self):
        """Метод check_win определяет комбинации для победе"""
        win_combination = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                           (0, 3, 6), (1, 4, 7), (2, 5, 8),
                           (0, 4, 8), (2, 4, 6))
        for comb in win_combination:
            if all(self.cells[cell].number == self.cells[comb[0]].number for cell in comb):
                return True
        return False

    def check_busy(self, number):
        """Метод check_busy устанавливает, что клетка занята"""
        if self.cells[number - 1].occupied:
            return True
        return False

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.win = False

    def go_cell(self, number, cells):
        """Метод go_cell определяет занята ли клетка и если нет присваивает символ игрока"""
        board.cells[number - 1].occupied = True
        board.cells[number - 1].number = self.symbol


class Game:
    def __init__(self):
        self.board = Board()

    def one_move(self, player):
        """алгоритм одного хода игрока"""
        try:
            number = int(input(f'{player.name} ходит - {player.symbol} (клетка от 1 до 9): '))
            if 1 <= number <= 9:
                if board.check_busy(number):
                    print('Клетка занята!')
                    self.one_move(player)
                else:
                    player.go_cell(number, board)
            else:
                raise ValueError('Ошибка ввода клетки.')

        except ValueError as exc:
            print(exc)
            self.one_move(player)

def main():
    count = 0
    while True:
        board.display_board()
        if count % 2 == 0:
            game.one_move(player_1)
            if board.check_win():
                print(f'{player_1.name} победил!')
                break
        else:
            game.one_move(player_2)
            if board.check_win():
                print(f'{player_2.name} победил!')
                break
        count += 1
        if count == 9:
            print('Ничья.')
            break
    board.display_board()


if __name__ == '__main__':
    print("*" * 5, " Игра Крестики-нолики для двух игроков ", "*" * 5)
    player_1 = Player('player_1', 'X')
    player_2 = Player('player_2', 'O')
    board = Board()
    game = Game()
    main()
