# Exercise 1 : Built-in functions
def my_abs(x):
    """
    Return the absolute value of a number.

    Parameters:
        x (number): A number.

    Returns:
        number: The absolute value of x.
    """
    if x < 0:
        print(-x)
    print(x)


def my_int(x):
    """
    Convert a number or a string representation of a number to an integer.

    Parameters:
        x (number or str): A number or a string representation of a number.

    Returns:
        int: The converted integer.
    """
    print(int(x))


def my_input(prompt=''):
    """
    Read a line of input from the user and return it as a string.

    Parameters:
        prompt (str, optional): A string to display as a prompt. Defaults to an empty string.

    Returns:
        str: The input entered by the user.
    """
    print(input(prompt))


# -----------------------------------------------------------------------------------------------------
# 🌟 Exercise 2: Currencies

class Currency:
    def __init__(self, currency: str, amount: int):
        self.currency = currency
        self.amount = amount

    # Your code starts HERE

    def __str__(self):
        if self.amount > 1:
            return f"{str(self.amount)} {self.currency}s"
        elif self.amount == 1:
            return f"1 {self.currency}"
        else:
            raise ValueError("Amount needs to be bigger than 1.")

    def __int__(self):
        return self.amount

    def __repr__(self):
        if self.amount > 1:
            return f"{str(self.amount)} {self.currency}s"
        elif self.amount == 1:
            return f"1 {self.currency}"
        else:
            raise ValueError("Amount needs to be bigger than 1.")

    def __add__(self, other):
        # when we do object instance + int  | c1+5
        if isinstance(other, (int, float)):
            # we do not return as Currency object is we want to match the output in the instruction.
            return self.amount + other
        elif isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            return self.amount + other.amount

    def __iadd__(self, other):
        # when we do object instance += int  | c1+=5
        if isinstance(other, (int, float)):
            self.amount += other
        elif isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            self.amount += other.amount
        # we defined in __repr__. when called, result will follow the format in __repr__.
        return self


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))  # '5 dollar'
print(int(c1))  # 5
print(repr(c1))  # '5 dollar'
print(c1 + 5)  # 10
print(c1 + c2)  # 15
print(c1)  # '5 dollar'
c1 += 5
print(c1)  # '10 dollar'
c1 += c2
print(c1)  # '20 dollar'
print(c1 + c3)
