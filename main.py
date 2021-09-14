import pygame, sys
import random


class Program:
    def __init__(self):
        self.name = "Faris"
        self.rnd_num = random.randint(1, 100)

    def run(self):
        pass

    def calculate(self):
        return pow(self.rnd_num, 2) * self.rnd_num

    def print_hi(self):
        print(f'Hi, {self.name}')
        print(f"This is a github testing program spesifically used for Pycharm if possibe")
        print("Anyway, here's a random number for no reason:")
        print(self.calculate())

    def print_a_smiley_face(self):
        print("Now I will print a smiley face")
        print(":)")
        print("Also, here's the random number: " + str(self.rnd_num))


if __name__ == '__main__':

    # Initialize pygame
    pygame.init()
    screen_width = 800
    screen_height = 400
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    icon = pygame.image.load('number_game.png')

    # Initiate instances
    program = Program()

    # Set caption, icon, color
    pygame.display.set_caption("Better Formatting: Number Game!")
    pygame.display.set_icon(icon)

    # Main loop (runs every tick) -------------------------------------------------
    while True:
        # Event code
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Game code
        program.run()

        # Updates, mind the order
        pygame.display.flip()
        screen.fill((50, 50, 50))

        # Time & Clock
        clock.tick(60)
