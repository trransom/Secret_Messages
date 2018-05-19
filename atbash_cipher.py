# Atbash Cipher
from ciphers import Cipher
from collections import OrderedDict
import string

class Atbash(Cipher):

	forwards = OrderedDict(zip(string.ascii_lowercase, string.ascii_lowercase[::-1]))
	backwards = OrderedDict(zip(string.ascii_lowercase[::-1], string.ascii_lowercase))

	'''
		Allows the user to initialize the class by creating their own forwards and backwards dictionaries.
	'''
	def __init__(self, forwards=OrderedDict(zip(string.ascii_lowercase, string.ascii_lowercase[::-1])),
				backwards=OrderedDict(zip(string.ascii_lowercase[::-1], string.ascii_lowercase))):
		self.forwards = forwards
		self.backwards = backwards

	'''
		Encrypts the given string by running it against the backwards dictionary.
	'''
	def encrypt(self, string):
		ans_string = [self.backwards[char] for char in string]
		ans = ''.join(ans_string)
		return ans

	'''
		Decrypts the given string by running it against the forwards dictionary.
	'''
	def decrypt(self, string):
		ans_string = [self.forwards[char] for char in string]
		ans = ''.join(ans_string)
		return ans
