# Atbash Cipher
from collections import OrderedDict
import string
from ciphers import Cipher


class Atbash(Cipher):
	
	alph1 = string.ascii_lowercase + ' '
	alph2 = string.ascii_lowercase[::-1] + ' '
	forwards = OrderedDict(zip(alph1, alph2))
	backwards = OrderedDict(zip(alph2, alph1))

	
	def __init__(self):
		'''
		Allows the user to initialize the class by creating their own forwards and backwards dictionaries.
		'''
		super().__init__('placeholder', self.forwards, self.backwards)
