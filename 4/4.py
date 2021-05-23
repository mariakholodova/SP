from multiprocessing import Process
from random import randint, uniform
from time import sleep


class Team:  # создаем чертеж класса для команд
    def __init__(self, name):  # конструктор. Принимает в себя имя команды
        self.fighters = 50     # устанавливаем количество бойцов на старте в команде
        self.name = name       # устанавливаем имя команды
        self.enemy = None      # создаем место под противника

    def call_new_figters(self):  # метод для "призыва" новых бойцов в команду
        self.fighters += randint(5, 10)  # к бойцам добавляется случайное число от 5 до 10

    def fight_enemy(self):  # метод для "удара" вражеской команды
        if self.enemy.fighters <= 0:  # если вражеская команда уже повержена
            print('Enemy already dead')  # то лежачих не бьют, пишем об этом
            return  # выходим из программы
        self.enemy.fighters -= int(self.fighters * uniform(0.1, 0.3))
        # уменьшаем количество бойцов врага на рандомное число (почти)

    def do_actions(self):  # метод для основных действий
        while True:  # в бесконечном цикле
            if self.fighters <= 0:  # если уже нет бойцов
                break  # перестаем драться
            print(f'Team {self.name} now have {self.fighters} fighters')  # выводим сколько бойцов у нас
            print(f'Enemy {self.enemy.name} now have {self.enemy.fighters} fighters')  # выводим сколько бойцов у противника
            self.call_new_figters()  # позвать новых бойцов
            self.fight_enemy()  # ударить врага
            if self.enemy.fighters <= 0:  # если у врага 0 бойцов - ура победа
                print(f'Team {self.name} won')  # выводим сообщение о победе
                break  # перестаем драться

            sleep(1)  # ждем 1 секунду (типа замахиваемся заново)


def controller():  # вторая программа - которая будет вызывать первую программу, ы
    team_a = Team('A')  # создаем команду А
    team_b = Team('B')  # создаем команду Б

    team_b.enemy = team_a  # устанавливаем, что противник команды Б это А
    team_a.enemy = team_b  # устанавливаем, что противник команды А это Б

    proc_b = Process(target=team_b.do_actions)  # создаем процесс для команды Б
    proc_a = Process(target=team_a.do_actions)  # создаем процесс для команды А

    proc_b.start()  # запускаем процесс для команды Б
    proc_a.start()  # запускаем процесс для команды А

    proc_b.join()  # дожидаемся завершения процесса для команды Б
    proc_a.join()  # дожидаемся завершения процесса для команды А


if __name__ == '__main__':
    controller()
