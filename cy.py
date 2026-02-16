import random 
import string 
chars = " "+string.punctuation + string.digits + string.ascii_letters
chars = list(chars) 
key = chars.copy() 
random.shuffle(chars)

print(f"Chars:{chars}")
print(f"Keys:{key}")
#ENCRYPTION
plain_text = input("Enter the message to encrypt:")
cipher_text = "" 
for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]
print(plain_text)
print(cipher_text)

# DECRYPTION
cipher_text = input("Enter the message to decrypt:")
plain_text = "" 
for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]
print(cipher_text)
print(plain_text)

