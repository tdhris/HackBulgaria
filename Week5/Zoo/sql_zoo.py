import sqlite3
from zoo_class import Zoo
from animals import Animal


class SQLAdapter:
    def __init__(self):
        self.connection = sqlite3.connect("zoos.db")
        self.cursor = self.connection.cursor()

    def load_zoos(self):
        zoos = {}

        #take all zoo ids
        self.cursor.execute("SELECT id FROM zoos")
        zoo_ids = [unparsed_id[0] for unparsed_id in self.cursor.fetchall()]

        #load the zoos
        for zoo_id in zoo_ids:
            zoo = self.load_zoo(zoo_id)
            zoos[zoo_id] = zoo
        return zoos

    def save_zoo(self, zoo):
        capacity = zoo.capacity
        budget = zoo.budget
        animal_count = zoo.animal_count

        self.cursor.execute("INSERT INTO zoos(budget, capacity, animal_count)\
            VALUES (?, ?, ?)", (budget, capacity, animal_count))
        zoo_id = self.cursor.lastrowid

        self.connection.commit()
        return zoo_id

    def load_zoo(self, zoo_id):
        #get zoo details
        self.cursor.execute("SELECT budget, capacity, animal_count FROM zoos\
                             WHERE id = ?", (zoo_id,))
        unparsed_zoo = self.cursor.fetchall()[0]

        budget = int(unparsed_zoo[0])
        capacity = int(unparsed_zoo[1])
        zoo = Zoo(budget, capacity)

        #get all animals in the zoo
        self.cursor.execute("SELECT animal_id FROM zoo_animals\
                             WHERE zoo_id = ?", (zoo_id,))
        animal_ids = [id[0] for id in self.cursor.fetchall()]
        animals = {}

        for animal_id in animal_ids:
            animal = self.load_animal(animal_id)
            if animal is not None:
                animals[animal_id] = animal
        zoo.animals = animals
        return zoo

    def update_zoo(self, zoo_id, zoo):
        self.cursor.execute("UPDATE zoos SET budget = ?\
                             WHERE id = ?", (zoo.budget, zoo_id))
        self.cursor.execute("DELETE FROM zoo_animals\
                             WHERE zoo_id = ?", (zoo_id,))
        for animal_id in zoo.animals.keys():
            self.add_animal_to_zoo(zoo_id, animal_id)
        self.connection.commit()

    def add_animal_to_zoo(self, zoo_id, animal_id):
        self.cursor.execute("INSERT INTO zoo_animals(zoo_id, animal_id)\
                             VALUES (?, ?)", (zoo_id, animal_id))
        self.cursor.execute("UPDATE zoos SET animal_count = animal_count + 1")
        self.connection.commit()

    def load_animal(self, animal_id):
        #get animal details
        self.cursor.execute("SELECT specie, name, age, weight, gender\
                             FROM animals WHERE id = ?", (animal_id,))
        unparsed_animal = self.cursor.fetchone()
        if unparsed_animal is None:
            return None

        specie = unparsed_animal[0]
        name = unparsed_animal[1]
        age = unparsed_animal[2]
        weight = unparsed_animal[3]
        gender = unparsed_animal[4]
        dead_or_alive = 1

        animal = Animal(specie, name, age, weight,
                        dead_or_alive, gender)
        animal.gender = gender

        return animal

    def remove_animal_from_zoo(self, zoo_id, animal_id):
        self.cursor.execute("DELETE FROM zoo_animals\
                             WHERE zoo_id = ? and animal_id = ?",
                            (zoo_id, animal_id))
        self.cursor.execute("DELETE FROM animals\
            WHERE id = ?", (animal_id,))
        self.connection.commit()

    def remove_animal(self, animal_id):
        self.cursor.execute("DELETE FROM animals\
            WHERE id = ?", (animal_id,))
