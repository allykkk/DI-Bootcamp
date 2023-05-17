import random


# 🌟 Exercise 1 – Random Sentence Generator

# Create a function called get_words_from_file. This function should read the file’s content and return the words as a collection.
def get_words_from_file():
    try:
        with open('sowpods.txt', 'r') as file:
            return file.read().splitlines()
    except:
        return []


# Create another function called get_random_sentence which takes a single parameter called length.
def get_random_sentence(length):
    words = get_words_from_file()
    # in case user required length is bigger than the words size
    if length > len(words): length = len(words)
    sentence = ' '.join(random.sample(words, length))
    return sentence.lower().capitalize()


# Create a function called main
def main():
    # Print a message explaining what the program does.
    print(
        "This is a Random Sentence Generator that generates a random sentence based on the number of words you choose.")

    # Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20.
    # assume user gives good input as number
    length = int(input("How long do you want the random sentence to be: "))
    # If the user inputs correct data, run your code.
    if length in range(0, 21):
        print("Generated Sentence: ", get_random_sentence(length))
    # If the user inputs incorrect data, print an error message and end the program.
    else:
        print("Error! Exit the program! ")


main()

# ----------------------------------------------------------------------------------------
# 🌟 Exercise 2: Working with JSON

import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

data = json.loads(sampleJson)
print(data)

# Access the nested “salary” key from the JSON-string above.
salary = data['company']['employee']["payable"]["salary"]
print("Salary:", salary)

data["company"]["employee"]["birth_date"] = "1990-01-01"
print(data)

with open("working_with_json.json", "w") as f:
    json.dump(data, f)
print("Saved")
