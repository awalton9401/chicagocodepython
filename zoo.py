class Animal:
    def __init__(self, animal_name, age):
        self.animal_name = animal_name
        self.age = age
        self.animal_health = 0
        self.animal_happiness = 0

    def feed(self):
        raise NotImplementedError

    def display_info(self):
        print(self.animal_name, self.animal_health, self.animal_happiness, self.age)


class Lion(Animal):
    def __init__(self, animal_name, age):
        super().__init__(animal_name, age)
        self.has_mane = True
        self.animal_health = 2
        self.animal_happiness = 4


    def feed(self):
        self.animal_happiness += 10
        self.animal_health += 10

        print(self.animal_name,"has been fed")

        return self
        

class Tiger(Animal):
    def __init__(self, animal_name, age):
        super().__init__(animal_name, age)
        self.attribute = "has strip"
        self.animal_health = 4
        self.animal_happiness = 5

        print(f"attribute:{self.attribute}")
    
    def feed(self):
        self.animal_happiness += 10
        self.animal_health += 10

        print(f"{self.animal_name} has been fed")

        return self

class Bear(Animal):
    def __init__(animal_name, age):
        super().__init__(animal_name, age)
        self.attribute = "has strip"
        self.animal_health = 2
        self.animal_happiness = 1

        print(f"attribute:{self.attribute}")
    
    def feed(self):
        self.animal_happiness += 10
        self.animal_health += 10

        print(f"{self.animal_name} has been fed")

        return self
        


class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_lion(self, name, age):
        self.animals.append(Lion(name, age))

        return self.animals[-1]

    def add_tiger(self, name, age):
        self.animals.append(Tiger(name, age))

        return self

    def print_all_info(self):

        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()


zoo1 = Zoo("Dre's Zoo")


zoo1.add_lion("Nala", 4)
zoo1.add_lion("Simba", 3)
zoo1.print_all_info()
zoo1.add_lion("Nala", 4).feed()
zoo1.add_lion("Simba", 3).feed()
zoo1.print_all_info()
zoo1.add_tiger("Rajah", 2)
zoo1.add_tiger("Shere Khan", 1)

        

        

        

    
