# Ciphers
from collections import OrderedDict
import string

class Cipher():

	alphabet = string.ascii_lowercase + ' '
	crypt_alphabet = 'enhgtwmbcdsojlfkzqyruviaxp '
	encrypt_dict = OrderedDict(zip(alphabet, crypt_alphabet))
	decrypt_dict = OrderedDict(zip(crypt_alphabet, alphabet))
	
	'''
		Initializes the cipher by allowing the user to 
		specify their own alphabet that gets run against
		the regular alphabet.
	'''
	def __init__(self, crypt_alphabet, encrypt_dict, decrypt_dict):
		self.message = message
		self.crypt_alphabet = crypt_alphabet
		self.encrypt_dict = encrypt_dict
		self.decrypt_dict = decrypt_dict
		
	'''
		Encrypts a message
	'''
	def encrypt(self, message):
		ans = ''
		for char in message:
			ans += encrypt_dict[char]
		return ans

	'''
		Decrypts a message
	'''
	def decrypt(self, message):
		ans = ''
		for char in message:
			ans += decrypt_dict[char]
		return ans
		