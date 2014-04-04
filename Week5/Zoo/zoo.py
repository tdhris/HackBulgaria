from command_parser import CommandParser
from sql_zoo import SQLAdapter
from zoo_class import Zoo
from animals import Animal
from calculate_time import period_to_days
import sys
import os


class ZooSimulator:
    def __init__(self):
        self.zoos = {}

        self.parser = CommandParser()
        self.adapter = SQLAdapter()
        self.load_functions()
        self.load_initial_state()
        self.simulator_loop()

    def create_zoo(self, arguments):
        capacity = int(input("capacity> "))
        budget = int(input('budget> '))
        zoo = Zoo(capacity, budget)
        zoo_id = self.adapter.save_zoo(zoo)
        self.zoos[zoo_id] = zoo

    def list_zoos(self, arguments):
        for zoo_id, zoo in self.zoos.items():
            print("[{0}] - {1}".format(zoo_id, zoo))

    def see_animals(self, arguments):
        zoo_id = int(arguments[0])
        zoo = self.zoos[zoo_id]
        for animal in zoo.animals.values():
            print(animal)

    def accommodate(self, arguments):
        zoo_id = int(arguments[0])
        zoo = self.zoos[zoo_id]

        species = input("species> ")
        name = input("name> ")
        age = input("age> ")
        weight = input("weight> ")
        animal = Animal(species, name, int(age), int(weight))
        animal_id = animal.insert_animals()

        self.adapter.add_animal_to_zoo(zoo_id, animal_id)
        zoo.accomodate_animal(animal_id, animal)

    def move_to_habitat(self, arguments):
        zoo_id = int(arguments[0])

        species = input("species> ")
        name = input("name> ")

        for animal_id in self.zoos[zoo_id].animals:
            animal = self.zoos[zoo_id].animals[animal_id]
            a_id = animal_id
            if animal.name == name and animal.specie == species:
                break

        del self.zoos[zoo_id].animals[a_id]
        self.adapter.remove_animal_from_zoo(zoo_id, a_id)
        self.adapter.remove_animal(animal_id)

    def simulate(self, arguments):
        zoo_id = int(arguments[0])
        interval_of_time = input("time interval (days / months / years)> ")
        period = int(input("period (how many days/months/years> "))

        days = int(period_to_days(interval_of_time, period))
        self.zoos[zoo_id].simulate_time(days)
        self.adapter.update_zoo(zoo_id, self.zoos[zoo_id])

    def exit(self, arguments):
        sys.exit(0)

    def load_initial_state(self):
        self.zoos = self.adapter.load_zoos()

    def load_functions(self):
        self.parser.add_function("create_zoo", self.create_zoo)
        self.parser.add_function("list_zoos", self.list_zoos)
        self.parser.add_function("see_animals", self.see_animals)
        self.parser.add_function("accommodate", self.accommodate)
        self.parser.add_function("move_to_habitat", self.move_to_habitat)
        self.parser.add_function("simulate", self.simulate)
        self.parser.add_function("exit", self.exit)

    def simulator_loop(self):
        while True:
            command = input("> ")
            self.parser.take_command(command)


if __name__ == '__main__':
    os.system("python3 create_databases_for_zoo.py")
    os.system("python3 create_animals_database.py")
    ZooSimulator()
