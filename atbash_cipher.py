# Atbash Cipher
from collections import OrderedDict
import string
from ciphers import Cipher


class Atbash(Cipher):
	
	alph1 = string.ascii_lowercase + ' '
	alph2 = string.ascii_lowercase[::-1] + ' '
	forwards = OrderedDict(zip(alph1, alph2))
	backwards = OrderedDict(zip(alph2, alph1))

	'''
		Allows the user to initialize the class by creating their own forwards and backwards dictionaries.
	'''
	def __init__(self):
		super().__init__('placeholder', self.forwards, self.backwards)

	'''
		Encrypts the given string by running it against the backwards dictionary.
	'''
#	def encrypt(self, string):
#		self.backwards[' '] = ' '
#		ans_string = [self.backwards[char] for char in string]
#		ans = ''.join(ans_string)
#		return ans

	'''
		Decrypts the given string by running it against the forwards dictionary.
	'''
#	def decrypt(self, string):
#		self.forwards[' '] = ' '
#		ans_string = [self.forwards[char] for char in string]
#		ans = ''.join(ans_string)
#		return ans
