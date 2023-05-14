# 🌟 Exercise 3 : Dogs Domesticated

import random

# Create a new python file and import your Dog class from the previous exercise.
from Day2.Day2_XP import Dog


# In the new python file, create a class named PetDog that inherits from Dog.
class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *dog_names):
        print(f"{', '.join(dog_names)} all play together")

    def do_a_trick(self):
        action = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
        if self.trained:
            print(f"{self.name} {random.choice(action)}")
        else:
            print(f"{self.name} is not trained yet.")


# Create an instance of PetDog
my_dog = PetDog(name="Luna", age=3, weight=12)
# Call the parent bark method
print(my_dog.bark())
# not trained yet
my_dog.do_a_trick()
# Call the train method
my_dog.train()
# Call the play method
my_dog.play("Rufus", "Max", "Lola")  # Output: Rufus, Max, Lola all play together
# Call the do_a_trick method
my_dog.do_a_trick()
