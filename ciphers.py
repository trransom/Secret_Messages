# Ciphers
from collections import OrderedDict
import string

class Cipher():

	alphabet = string.ascii_lowercase
	crypt_alphabet = 'enhgtwmbcdsojlfkzqyruviaxp '
	encrypt_dict = OrderedDict(zip(alphabet, crypt_alphabet))
	decrypt_dict = OrderedDict(zip(crypt_alphabet, alphabet))
	
	
	def __init__(self,
				crypt_alphabet='enhgtwmbcdsojlfkzqyruviaxp ', 
				encrypt_dict=OrderedDict(zip(alphabet, crypt_alphabet)), 
				decrypt_dict=OrderedDict(zip(crypt_alphabet, alphabet))):
		'''
		Initializes the cipher by allowing the user to specify 
		their own alphabet that gets run against
		the regular alphabet.
		'''
		self.crypt_alphabet = crypt_alphabet
		self.encrypt_dict = encrypt_dict
		self.decrypt_dict = decrypt_dict
		
	
	def encrypt(self, message):
		'''Encrypts a message.'''
		ans = ''
		for char in message:
			ans += str(self.encrypt_dict[char])
		return ans

	
	def decrypt(self, message):
		'''Decrypts a message.'''
		ans = ''
		for char in message:
			ans += self.decrypt_dict[char]
		return ans
		