# Exercise 1 : Family

# Create a class called Family and implement the following attributes:
class Family():
    def __init__(self, members: list, last_name: str):
        # members: list of dictionaries with the following keys : name, age, gender and is_child (boolean).
        self.members = members
        self.last_name = last_name

    def born(self, **kwargs):
        kwargs['is_child'] = True
        self.members.append(kwargs)
        print(f"Congratulations on the new baby, {kwargs['name']} {self.last_name}!")

    def is_18(self, check_member):
        for member in self.members:
            if member['name'] == check_member:
                if member['age'] >= 18: return True
        return False

    def family_presentation(self):
        print(f"Family <{self.last_name}> has family members: {', '.join(member['name'] for member in self.members)}.")


my_family = Family(last_name="Smith", members=[
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
])

my_family.born(name="Max", age=0, gender="Female")
print(my_family.is_18("Michael"))  # True
print(my_family.is_18("Max"))  # False
my_family.family_presentation()
print("\n")


# -------------------------------------------------------------------------------------------------------------------
# Exercise 2 : The Incredibles Family
class TheIncredibles(Family):
    def __init__(self, last_name, members):
        super().__init__(members,last_name)

    def use_power(self, member_name):
        for member in self.members:
            if member['name'] == member_name:
                # use function from parent object is_18() to check if the member is over 18 years old.
                if self.is_18(member_name):
                    print(f"{member_name} can use their power: {member['power']}")
                else:
                    raise Exception(f"{member_name} is not over 18 years old and cannot use their power.")

    def incredible_presentation (self):
        super().family_presentation()
        for member in self.members:
            print(f"{member['name']} is {member['incredible_name']} and their power is {member['power']}")


incredibles = TheIncredibles(last_name="Anderson", members=[
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds',
     'incredible_name': 'SuperWoman'}
])


# Call incredible_presentation method
incredibles.incredible_presentation()
# Use born method to add Baby Jack with power 'Unknown Power'
incredibles.born(name='Jack', age=0, gender='Male', is_child=True, power='Thunder', incredible_name='JackTheThunder')
# Call incredible_presentation method again
incredibles.incredible_presentation()
# check use_power method
incredibles.use_power('Michael')
# check use_power method  (exception expected)
incredibles.use_power('Jack')