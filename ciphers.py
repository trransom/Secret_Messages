# Ciphers
from collections import OrderedDict
import string

class Cipher

	alphabet = string.ascii_lowercase
	crypt_alphabet = 'enhgtwmbcdsojlfkzqyruviaxp'
	encrypt_dict = OrderedDict(zip(alphabet, crypt_alphabet))
	decrypt_dict = OrderedDict(zip(crypt_alphabet, alphabet))
	
	def __init__(self, crypt_alphabet):
		self.message = message
		self.crypt_alphabet = crypt_alphabet
		
		
	def encrypt(self, message):
		ans = ''
		for char in message:
			ans += encrypt_dict[char]
		return ans
		
	def decrypt(self, message):
		ans = ''
		for char in message:
			ans += decrypt_dict[char]
		return ans
		