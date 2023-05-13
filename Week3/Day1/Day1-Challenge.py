# Create a class called Farm. How should it be implemented?


class Farm:
    def __init__(self, name):
        self.name = name
        self.animal_dict = {}

    def add_animal(self, animal: str, amount: int = 1):
        if animal not in self.animal_dict.keys():
            self.animal_dict[animal] = amount
        else:
            self.animal_dict[animal] += amount

    def get_info(self):
        # just to make the output exactly like the given example
        result = f"{self.name}'s farm\n\n"
        for animal, amount in self.animal_dict.items():
            result += f"{animal} : {amount}\n"
        result += "\n    E-I-E-I-0!"
        return result

    # Expand The Farm
    #
    # Add a method called get_animal_types to the Farm class. This method should return a sorted list of all the
    # animal types (names) in the farm. With the example above, the list should be: ['cow', 'goat', 'sheep'].
    #
    # Add another method to the Farm class called get_short_info. This method should return the following string:
    # “McDonald’s farm has cows, goats and sheep.”. The method should call the get_animal_types function to get a
    # list of the animals.

    def get_animal_types(self):
        sorted_dict = {keys: self.animal_dict[keys] for keys in sorted(self.animal_dict.keys())}
        return [animal for animal in sorted_dict.keys()]

    def get_short_info(self):
        animal_list = self.get_animal_types()
        print(f"{self.name}'s farm has {', '.join(animal_list[:-1])} and {animal_list[-1]}.")


macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_animal_types())
macdonald.get_short_info()
