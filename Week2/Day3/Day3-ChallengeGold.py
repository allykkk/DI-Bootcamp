# Create a python program that encrypts and decrypts messages with ceasar cypher.

def encrypt_message(text):
    cypher_text = ""
    for letter in text:
        cypher_text += chr(ord(letter) + 3)
    return cypher_text


def decrypt_message(text):
    cypher_text = ""
    for letter in text:
        cypher_text += chr(ord(letter) - 3)
    return cypher_text


text = input("Type your original message: ")
print(f"The encrypted verisin of your message is : {encrypt_message(text)}.")
text = input("Type your encrpyted message: ")
print(f"The decrypted verisin of your message is : {decrypt_message(text)}.")
