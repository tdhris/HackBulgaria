import sqlite3
from random import randint

conn = sqlite3.connect("zoos.db")
cursor = conn.cursor()

NAMES = ["Leo", "Lea", "Maxi", "Kate", "Sam", "Tom", "Jenkins",
         "Lagrange", "Erbrane", "Ermite", "Pythagoras",
         "Neumann", "Fourier", "Weierstrass",
         "Dirichlet", "Hammilton", "Bessel",
         "Euler", "Sandy", "Pena"]

MONTH = 30


class Animal():
    def __init__(self, specie, name, age, weight,
                 dead_or_alive=1, gender=1,
                 time_since_last_birth=0, is_pregnant=0, time_pregnant=0):
        self.specie = specie
        #age is in months
        self.age = age
        self.name = name
        self.weight = weight
        self.dead_or_alive = dead_or_alive

        gender = randint(1, 100)
        if gender % 2:
            self.gender = 'm'
        else:
            self.gender = 'f'

        #attributes only of the female animals; should be in a subclass
        self.time_since_last_birth = time_since_last_birth
        self.is_pregnant = is_pregnant
        self.time_pregnant = time_pregnant

    def __repr__(self):
        if self.gender == 'm':
            gender = 'male'
        elif self.gender == 'f':
            gender = 'female'
        else:
            gender = 'error'

        return "{0} - species: {1}, age: {2}, weight: {3}, gender: {4}".format(self.name,
                                                                               self.specie,
                                                                               str(self.age),
                                                                               str(self.weight),
                                                                               gender)

    @property
    def chance_of_dying(self):
        """
        life_expectancy is multiplied by 2 and divided by the actual age
        before the animal reaches life_expectancy,chance of dying is below 50%,
        and after it's passed life_expectancy, its chance of dying is above 50%
        if its age reaches twice life_expectancy, its chance of dying is 100%
        """
        life_expectancy = self.get_life_expectancy()
        chance_of_dying = (self.age / (life_expectancy * 2)) * 100
        return chance_of_dying

    #fatter animals eat more and so they cost more
    @property
    def expense(self):
        query_lang = "SELECT food_type, food_weight_ratio FROM animals_general\
                      WHERE species = ?"

        food = tuple(cursor.execute(query_lang, (self.specie,)))
        food_type = food[0][0]
        food_weight_ratio = food[0][1]
        if food_type == 'carnivore':
            return int(self.weight * food_weight_ratio * 2)
        else:
            return int(self.weight * food_weight_ratio * 4)

    def can_breed(self):
        return self.gender == 'f'\
            and self.time_pregnant == 0\
            and self.enough_time_since_last_birth()

    def enough_time_since_last_birth(self):
        return self.time_since_last_birth >= 6 * MONTH\
            or self.time_since_last_birth == 0

    def get_life_expectancy(self):
        query_lang = "SELECT life_expectancy FROM animals_general\
                      WHERE species = ?"
        life_expectancy = cursor.execute(query_lang, (self.specie,))
        return tuple(life_expectancy)[0][0]

    #this should be used after the animal's been aged up
    def is_dead_or_alive(self):
        random_number = randint(1, 100)
        if random_number < self.chance_of_dying:
            return False
        else:
            return True

    def die(self):
        self.dead_or_alive = 0
        print("{} The {} died today.".format(self.name, self.specie))
        query_lang = "DELETE FROM animals WHERE name = ? and specie = ?"
        cursor.execute(query_lang, (self.name, self.specie))
        conn.commit()

    def is_over_average_weight(self):
        query_lang = "SELECT average_weight FROM animals_general\
                      WHERE species = ?"
        average_weight = cursor.execute(query_lang, (self.specie,))
        return self.weight >= tuple(average_weight)[0][0]

    def gain_weight(self, days):
        for day in range(days):
            if not self.is_over_average_weight():
                query_lang = "SELECT weight_age_ratio FROM animals_general\
                              WHERE species = ?"
                weight_age_ratio = cursor.execute(query_lang, (self.specie,))
                gain = tuple(weight_age_ratio)[0][0]
                self.weight += gain

    def insert_animals(self):
        cursor.execute("SELECT species FROM animals_general")
        correct_specie = [animal[0] for animal in cursor.fetchall()]
        if self.specie not in correct_specie:
            print("This is unknown creature. Sorry. Try again.")
            return
        query_lang = "INSERT INTO animals(specie, name, age, weight, gender,\
                      chance_of_dying, dead_or_alive)\
                      VALUES(?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(query_lang, (self.specie,
                                    self.name,
                                    self.age,
                                    self.weight,
                                    self.gender,
                                    self.chance_of_dying,
                                    self.dead_or_alive))
        query_id = "SELECT id FROM animals WHERE specie = ? AND name = ?"
        get_id = cursor.execute(query_id, (self.specie, self.name))
        id = tuple(get_id)[0][0]
        conn.commit()
        #returns the id from the animals db
        return id

    def update_animals(self, id):
        query_lang = "UPDATE animals SET age = ?, weight = ?,\
                      chance_of_dying = ?, dead_or_alive = ? WHERE id = ?"
        cursor.execute(query_lang, (self.age, self.weight,
                                    self.chance_of_dying,
                                    self.dead_or_alive, id))
        conn.commit()

    def give_birth(self):
        self.time_since_last_birth = 1
        name = randint(0, len(NAMES) - 1)

        query_lang = "SELECT newborn_weight FROM animals_general\
                      WHERE species = ?"
        newborn_weight = cursor.execute(query_lang, (self.specie,))

        newborn = Animal(self.specie, "{}".format(NAMES[name]), 0,
                         tuple(newborn_weight)[0][0])

        query_lang = "INSERT INTO animals(specie, name, age, weight, gender,\
                      chance_of_dying, dead_or_alive)\
                      VALUES(?, ?, ?, ?, ?, ?, ?)"

        cursor.execute(query_lang, (newborn.specie, newborn.name, newborn.age,
                                    newborn.weight, newborn.gender,
                                    newborn.chance_of_dying,
                                    newborn.dead_or_alive))
        newborn_id = cursor.lastrowid

        print("Newborn {} with name {} has been born today!".format(
            newborn.specie,
            newborn.name))
        conn.commit()
        return (newborn_id, newborn)

    def grow_older(self, days):
        #age is in months
        self.age += round(days / 30, 2)
        self.gain_weight(days)

    def get_gestation(self):
        cursor.execute("SELECT gestation FROM animals_general\
                        WHERE species = ?", (self.specie,))
        gestation_period = cursor.fetchone()[0]
        return gestation_period

    def get_pregnant(self):
        self.is_pregnant = 1
        self.time_pregnant = 0

    def breed(self, days):
        gestation = self.get_gestation() * MONTH
        births = 0

        for day in range(days):
            self.time_since_last_birth += 1
            if not self.enough_time_since_last_birth():
                pass
            elif self.enough_time_since_last_birth():
                if self.is_pregnant == 0:
                    self.get_pregnant()
                elif self.time_pregnant >= gestation:
                    births += 1
                    self.time_since_last_birth = 0
                    self.is_pregnant = 0
                elif self.is_pregnant == 1 and self.time_pregnant <= gestation:
                    self.time_pregnant += 1

        return births
