import random 
import string
chars ="" + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)
print(f"chars:{chars}")
print(f"key:{key}")
plain_text = input("Enter the plain text(A-Z):")
cipher_text =""
for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]
    print(cipher_text)
    print(plain_text)