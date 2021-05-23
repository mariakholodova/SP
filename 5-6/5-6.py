from random import randint, uniform
from threading import Thread, Lock
from time import sleep

print_lock = Lock()  # мьютекс для работы с разделяемым ресурсом


class Team:
    def __init__(self, name):
        self.fighters = 50
        self.name = name
        self.enemy = None

    def call_new_figters(self):
        self.fighters += randint(5, 10)

    def fight_enemy(self, enemy):
        if enemy.fighters <= 0:
            print_lock.acquire()  # заблокировать мьютекс
            print('Enemy already dead')
            print_lock.release()  # разблокировать мьютекс
            return
        enemy.fighters -= int(self.fighters * uniform(0.3, 0.4))

    def do_actions(self):
        while True:
            if self.fighters <= 0:
                return
            print_lock.acquire()  # заблокировать мьютекс
            print(f'Team {self.name} now have {self.fighters} fighters')
            print_lock.release()  # разблокировать мьютекс
            self.call_new_figters()
            self.fight_enemy(self.enemy)
            if self.enemy.fighters <= 0:
                print_lock.acquire()  # заблокировать мьютекс
                print(f'Team {self.name} won')
                print_lock.release()  # разблокировать мьютекс
                return
            sleep(0.01)


if __name__ == '__main__':
    team_a = Team('A')
    team_b = Team('B')

    team_b.enemy = team_a
    team_a.enemy = team_b

    th_a = Thread(target=team_a.do_actions)
    th_b = Thread(target=team_b.do_actions)
    th_a.start()
    th_b.start()

    th_b.join()
    th_a.join()
