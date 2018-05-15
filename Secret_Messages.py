#Secret Messages
from ciphers import Cipher
from atbash_cipher import Atbash
from polybius_cipher import Polybius
from keyword_cipher import Keyword

print("This is a Secret Messages program. Choose your cipher and encrypt or decrypt your message!\n\n")
print("These are the current ciphers available:\n\n-Atbash\n-Hill\n-Polybius\n\n")
code = input("Which cipher would you like to use?\n").toLower()

key = Keyword()
print(key.encrypt('kryptos', 'knowledge'))
print(key.decrypt('kryptos', 'dghvetpst'))

#class crpytography(Cipher):

