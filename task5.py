import random


class CandyMan:
    def __init__(self):
        self.sticks = []
        self.total_size = 0
        self.red_sticks = 0
        self.total_number = 0

    def add_candy(self):
        size = random.randint(1, 100)
        red = random.choice([True, False])
        self.total_size += size
        self.sticks.append([size, red])
        self.total_number += 1
        if red:
            self.red_sticks += 1

    def get_a_random_candy(self):
        i = random.randint(0, len(self.sticks)-1)
        rm = self.sticks[i]
        self.total_number -= 1
        self.total_size -= rm[0]
        if rm[1]:
            self.red_sticks -= 1
        self.sticks.remove(self.sticks[i])
        return rm

    def get_average_size(self):
        return self.total_size / self.total_number

    def get_red_candy_chance(self):
        return self.red_sticks / self.total_number * 100
