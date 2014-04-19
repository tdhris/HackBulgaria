from command_parser import CommandParser
from dungeon import Dungeon
from time import sleep
from os import system
from hero import Hero


class Game:
    def __init__(self):
        self.parser = CommandParser()
        self.load_functions()
        self.run()

    def initialize_game(self):
        name = input("Character Name> ")
        health = 100
        nickname = input("Character Nickname> ")
        self.hero = Hero(name, health, nickname)
        self.level = 1
        self.map = Dungeon()
        self.map.spawn(self.hero)

    def run(self):
        running = True
        system('clear')
        print("Welcome to Dungeons & Pythons!")
        print("What are you waiting for? Create your character and start slaying...")
        self.initialize_game()
        print("Loading Level " + str(self.level) + '...')
        sleep(3)

        while running:
            system('clear')
            if not self.hero.is_alive():
                print("\n\nGAME OVER!")
                sleep(3)
                self.run()

            print("Character: {0}".format(str(self.hero)))
            print("Health: {0}".format(str(self.hero.get_health())))
            print("Weapon: {0}".format(str(self.hero.weapon)))
            print("Level: {0}".format(str(self.level)))
            print("\n")

            self.map.print_map()
            command = input("\nEnter direction <u, d, r, l>: ")
            self.parser.take_command(command)
            self.hero = self.map.hero
            if self.map.game_ended:
                system('clear')
                self.level += 1
                self.map = Dungeon(self.level)
                if not self.map.map:
                    print("YOU WON!!! Congratulations, Dungeon Master! ;)")
                self.map.spawn(self.hero)
                print("Loading Level " + str(self.level) + '...')
                sleep(3)

    def move_up(self, arguments):
        self.map.move('up')

    def move_down(self, arguments):
        self.map.move('down')

    def move_right(self, arguments):
        self.map.move('right')

    def move_left(self, arguments):
        self.map.move('left')

    def load_functions(self):
        self.parser.add_function('u', self.move_up)
        self.parser.add_function('d', self.move_down)
        self.parser.add_function('r', self.move_right)
        self.parser.add_function('l', self.move_left)


def main():
    Game()


if __name__ == '__main__':
    main()
