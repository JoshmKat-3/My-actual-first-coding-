import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#ENCRYPT
plain_text = input("What would you like to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"The Original message : {plain_text}")
print(f"Encrypted message: {cipher_text}")

#DECRYPT
cipher_text = input("What would you like to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"The encrypted message: {cipher_text}")
print(f"The decrypted message: {plain_text}")