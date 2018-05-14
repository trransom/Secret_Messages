# Atbash Cipher
from ciphers import Cipher
from collections import OrderedDict
import string

class Atbash(Cipher):
#    backwards = {number: letter for letter, number in zip('abcdefghijklmnopqrstuvwxyz'[::-1], range(1, 27))}
#	forwards = {number: letter for letter, number in zip('abcdefghijklmnopqrstuvwxyz', range(1, 27))}
	forwards = OrderedDict(zip(string.ascii_lowercase, string.ascii_lowercase[::-1]))
	backwards = OrderedDict(zip(string.ascii_lowercase[::-1], string.ascii_lowercase))

	def __init__(self):
		pass

	def encrypt(self, string):
		ans = ''
		for char in string:
			new_char = self.backwards[char]
			ans += new_char
		return ans

	def decrypt(self, string):
		ans = ''
		for char in string:
			new_char = self.forwards[char]
			ans += new_char
		return ans
