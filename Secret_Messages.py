#Secret Messages
from ciphers import Cipher
from atbash_cipher import Atbash
from polybius_cipher import Polybius
from keyword_cipher import Keyword

def encrypt(code, string):
	if code=='atbash':
		atbash = Atbash()
		return atbash.encrypt(string)
	elif code=='polybius':
		poly = Polybius()
		return poly.encrypt(string)
	elif code=='keyword':
		key = Keyword()
		return key.encrypt('kryptos', string)
		
def decrypt(code, string):
	if code=='atbash':
		atbash = Atbash()
		return atbash.decrypt(string)
	elif code=='polybius':
		poly = Polybius()
		return poly.decrypt(string)
	elif code=='keyword':
		key = Keyword()
		return key.decrypt('kryptos', string)


print("This is a Secret Messages program. Choose your cipher and encrypt or decrypt your message!\n\n")
print("These are the current ciphers available:\n\n-Atbash\n-Hill\n-Polybius\n\n")
code = input("Which cipher would you like to use?\n").lower()
message = input("What message would you like to encrypt or decrypt?\n")
crypt = input("Excellent. Would you like to encrypt or decrypt?\n").lower()

if crypt=='encrypt':
	answer = encrypt(code, message)
	print(answer)
elif crypt=='decrypt':
	answer = decrypt(code, message)
	print(answer)

#class crpytography(Cipher):

