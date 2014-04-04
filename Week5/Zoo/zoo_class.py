animal_earnings = 60


#add is_there_a_male animal from teh same species
class Zoo:
    def __init__(self, capacity, budget):
        self.capacity = capacity
        self.budget = budget
        self.animals = {}

    def __repr__(self):
        return "{0}: ({1}, {2})".format('Zoo', self.capacity, self.budget)

    @property
    def animal_count(self):
        return len(self.animals)

    def accomodate_animal(self, animal_id, animal):
        if self.budget == 0:
            return False
        self.animals[animal_id] = animal
        return True

    def calculate_gains(self):
        #for animal in animals deduct costs and add $60
        gains = 0
        for animal in self.animals.values():
            #animal_earnings is a constant; $60
            gains += animal_earnings
            gains -= animal.expense
        return gains

    def simulate_time(self, days):
        #age up every animal and get dead animals
        dead_animals = []
        for animal_id, animal in self.animals.items():
            animal.grow_older(days)
            if not animal.is_dead_or_alive():
                dead_animals.append(animal_id)
                animal.die()
            else:
                animal.update_animals(animal_id)

        #get rid of dead animals
        for animal_id in dead_animals:
            del self.animals[animal_id]

        newborns = {}
        for animal in self.animals.values():
            if animal.can_breed() and self.is_there_male(animal.specie):
                births = animal.breed(days)
                for birth in range(births):
                    newborn_id, newborn = animal.give_birth()
                    newborns[newborn_id] = newborn

        for newborn_id, newborn in newborns.items():
            self.animals[newborn_id] = newborn
            animal.update_animals(animal_id)

        #add gains to budget
        gains = self.calculate_gains() * days
        self.budget += gains

    def is_there_male(self, species):
        for animal in self.animals.values():
            if animal.specie == species and animal.gender == 'm':
                return True
        return False
