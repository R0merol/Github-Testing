import random


class Program:
    def __init__(self):
        self.name = "Faris"
        self.rnd_num = random.randint(1, 100)

    def run(self):
        self.print_hi()
        print(self.calculate())

    def calculate(self):
        return pow(self.rnd_num, 2) * self.rnd_num

    def print_hi(self):
        print(f'Hi, {self.name}')
        print(f"This is a github testing program spesifically used for Pycharm if possibe")
        print("Anyway, here's a random number for no reason:")


if __name__ == '__main__':
    program = Program()
    program.run()
