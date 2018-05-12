#Secret Messages
from ciphers import Cipher
from atbash_cipher import Atbash

print("This is a Secret Messages program. Choose your cipher and encrypt or decrypt your message!\n\n")
print("These are the current ciphers available:\n\n-Atbash\n-Hill\n-Polybius\n\n")
input("Which cipher would you like to use?\n")
t = Atbash()
print(t.backwards)

#class crpytography(Cipher):

