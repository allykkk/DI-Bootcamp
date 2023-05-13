# 🌟 Exercise 1: Cats

#   Instantiate three Cat objects using the code provided above.
#   Outside of the class, create a function that finds the oldest cat and returns the cat.
#   Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


cat_one = Cat("Luna", 5)
cat_two = Cat("Leo", 3)
cat_three = Cat("Mocha", 1)


def find_oldest(cats):
    max_age = 0
    for cat in cats:
        if cat.age >= max_age:
            max_age = cat.age
            oldest_cat = cat
    return oldest_cat


oldest_cat = find_oldest([cat_one, cat_two, cat_three])
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")
print("\n")


# ------------------------------------------------------------------------------------
# 🌟 Exercise 2 : Dogs

# Create a class called Dog.
class Dog:
    # In this class, create an __init__ method that takes two parameters : name and height.
    def __init__(self, dog_name, dog_height):
        self.name = dog_name
        self.height = dog_height

    # Create a method called bark that prints the following string “<dog_name> goes woof!”.
    def bark(self):
        print(f"{self.name} goes woof!")

    # Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")


# Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
davids_dog = Dog("Rex", 50)
# Print the details of his dog (ie. name and height) and call the methods bark and jump.
print(davids_dog.name, davids_dog.height)
davids_dog.bark()
davids_dog.jump()

# Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
sarahs_dog = Dog("Teacup", 20)
# Print the details of her dog (ie. name and height) and call the methods bark and jump.
print(sarahs_dog.name, sarahs_dog.height)
sarahs_dog.bark()
sarahs_dog.jump()


# Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.
def bigger_dog(dog_a, dog_b):
    if dog_a.height > dog_b.height:
        print(f"{dog_a.name} is the bigger one! ")
    if dog_a.height == dog_b.height:
        print(f"{dog_a.name} is as big as {dog_b.name}")
    else:
        print(f"{dog_b.name} is the bigger one! ")


bigger_dog(davids_dog, sarahs_dog)
print("\n")


# ------------------------------------------------------------------------------------
# 🌟 Exercise 3 : Who’s the song producer?

# Define a class called Song, it will show the lyrics of a song.
class Song:
    # Its __init__() method should have two arguments: self and lyrics (a list).
    def __init__(self, lyrics: list):
        self.lyrics = lyrics

    # Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
    def sing_me_a_song(self):
        print("\n".join(self.lyrics))


# Create an object, for example:
stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()
print("\n")


# ------------------------------------------------------------------------------------
# Exercise 4 : Afternoon at the Zoo

# Create a class called Zoo.
class Zoo:
    # In this class create a method __init__ that takes one parameter: zoo_name.
    # It instantiates two attributes: animals (an empty list) and name (name of the zoo).
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    # Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
    def add_animal(self, *new_animals):
        for new_animal in new_animals:
            if new_animal not in self.animals:
                self.animals.append(new_animal)

    # Create a method called get_animals that prints all the animals of the zoo.
    def get_animal(self):
        print(f"These are the animals in the zoo: {' '.join(self.animals)}")

    # Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been successfully sold.")
        else:
            print(f"{animal_sold} is not in the zoo! The sale has failed. ")

    # Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
    def sort_animals(self):
        sorted_animals = {}
        for animal in sorted(self.animals):
            first_letter = animal[0]
            if first_letter in sorted_animals:
                sorted_animals[first_letter].append(animal)
            else:
                sorted_animals[first_letter] = [animal]
        grouped_animals = {}
        group_num = 1
        for key in sorted(sorted_animals.keys()):
            grouped_animals[group_num] = sorted_animals[key]
            group_num += 1
        return grouped_animals

    # Create a method called get_groups that prints the animal/animals inside each group.
    def get_groups(self, grouped_animals):
        for group_number, group_value in grouped_animals.items():
            print(f"Group {group_number} has animals: {' '.join(group_value)}")


ramat_gan_safari = Zoo("ramat_gan_safari")
ramat_gan_safari.add_animal("Ape", "Baboon", "Bear", "Cat", "Cougar", "Eel", "Emu", "Giraffe")
ramat_gan_safari.get_animal()
ramat_gan_safari.sell_animal("Bee")
ramat_gan_safari.sell_animal("Giraffe")
grouped_animals = ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups(grouped_animals)
