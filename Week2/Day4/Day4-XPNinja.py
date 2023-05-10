# Exercise 1 : What’s your name ?
def get_full_name(first_name, last_name, middle_name=None):
    # we can also create a list [first_name.capitalize(), last_name.capitalize()] to reduce duplicate /.capitalize()/
    # However creating a list costs more memory space than modifying strings
    if middle_name:
        full_name = f"{first_name.capitalize()} {middle_name.capitalize()} {last_name.capitalize()}"
    else:
        full_name = f"{first_name.capitalize()} {last_name.capitalize()}"
    print(full_name)


get_full_name(first_name="john", middle_name="hooker", last_name="lee")
get_full_name(first_name="bruce", last_name="lee")
print("\n")

# --------------------------------------------------------------------------------
# Exercise 2 : From English to Morse

# Dictionary representing the morse code chart
morse_code_dict = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}

# we need to translate space to "/"
morse_code_dict[" "] = "/"
# reverse the dict for decryption
reversed_morse_dict = {morse: letter for letter, morse in morse_code_dict.items()}


def morse_encrypt(sentence):
    encrypted_sentence = ""
    for letter in sentence:
        encrypted_sentence += morse_code_dict[letter.upper()] + " "
    return encrypted_sentence


def morse_decrypt(morse_code):
    original_sentence = ""
    for i in morse_code.split(" "):
        original_sentence += reversed_morse_dict[i]
    return original_sentence


test = "I love learning python."
print(morse_encrypt(test))

reversed_test = ".. / .-.. --- ...- . / .-.. . .- .-. -. .. -. --. / .--. -.-- - .... --- -. .-.-.-"
print(morse_decrypt(reversed_test))
print("\n")

# --------------------------------------------------------------------------------
# Exercise 3 : Box of stars

def box_printer(*args:str):
    # the column count of the box is decided by the longest string
    word_column_count=len(max(args, key=len))
    # 4 is from ** decoration both sides
    print("*"*(word_column_count+4))
    for i in args:
        print("* "+i+ (word_column_count - len(i))*" "+" *")
    print("*" * (word_column_count + 4))

box_printer("Hello", "World", "in", "reallylongword", "a", "frame")


