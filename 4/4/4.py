from multiprocessing import Process
from random import randint, uniform
from time import sleep


class Team:  # создаем чертеж класса для команд
    def __init__(self, name):
        self.fighters = 50
        self.name = name
        self.enemy = None

    def call_new_figters(self):
        self.fighters += randint(5, 10)

    def fight_enemy(self):
        if self.enemy.fighters <= 0:
            print('Enemy already dead')
            return
        self.enemy.fighters -= int(self.fighters * uniform(0.1, 0.3))

    def do_actions(self):  # метод для основных действий
        while True:
            if self.fighters <= 0:
                break  # перестаем
            print(f'Team {self.name} now have {self.fighters} fighters')
            print(f'Enemy {self.enemy.name} now have {self.enemy.fighters} fighters')
            self.call_new_figters()
            self.fight_enemy()
            if self.enemy.fighters <= 0:
                print(f'Team {self.name} won')
                break

            sleep(1)


def controller():
    team_a = Team('A')  # создаем команду А
    team_b = Team('B')

    team_b.enemy = team_a  # устанавливаем, что противник команды Б это А
    team_a.enemy = team_b

    proc_b = Process(target=team_b.do_actions)  # создаем процесс для команды Б
    proc_a = Process(target=team_a.do_actions)

    proc_b.start()  # запускаем процесс для команды Б
    proc_a.start()

    proc_b.join()  # дожидаемся завершения процесса для команды Б
    proc_a.join()


if __name__ == '__main__':
    controller()
