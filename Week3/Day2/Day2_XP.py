# 🌟 Exercise 1 : Pets
class Pets:
    def __init__(self, animals: list):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# Create another cat breed named Siamese which inherits from the Cat class.
class Siamese(Cat):
    pass


if __name__ == '__main__':
    # Create a list called all_cats, which holds three cat instances : one Bengal, one Chartreux and one Siamese.
    bengal = Bengal('Bengie', 2)
    chartreux = Chartreux('Charly', 4)
    siamese = Siamese('Simba', 3)
    all_cats = [bengal, chartreux, siamese]

    # Create an instance of the Pets class with all the cat instances
    sara_pets = Pets(all_cats)
    sara_pets.walk()
    print("\n")


# -------------------------------------------------------------------------------------------
# 🌟 Exercise 2 : Dogs

# Create a class called Dog with the following attributes name, age, weight.
class Dog():
    def __init__(self, name: str, age: int, weight: int):
        self.name = name
        self.age = age
        self.weight = weight

    # Implement the following methods in the Dog class:

    # bark: returns a string which states: “<dog_name> is barking”.
    def bark(self):
        return f"{self.name} is barking"

        # run_speed: returns the dogs running speed (weight/age*10)

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
            return f"{self.name} won the fight"
        elif self.run_speed() * self.weight < other_dog.run_speed() * other_dog.weight:
            return f"{other_dog.name} won the fight"
        else:
            return f"It is a even fight!"


if __name__ == '__main__':
    dog1 = Dog("Max", 3, 10)
    dog2 = Dog("Buddy", 5, 21)
    dog3 = Dog("Charlie", 2, 8)

    print(dog1.bark())
    print(dog2.run_speed())
    print(dog3.fight(dog1))

# -------------------------------------------------------------------------------------------
# 🌟 Exercise 3 : Dogs Domesticated

# the exercise needs to import file, please check file Day2-XP-ex3.py
# link is https://github.com/allykkk/DI-Bootcamp/blob/master/Week3/Day2/Day2-XP-ex3.py
