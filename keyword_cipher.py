# Keyword cipher
from ciphers import Cipher
import string

alphabet = string.ascii_lowercase
key_list = []
alph_dict = {}

class Keyword(Cipher):
	
	def __init__(self):
		pass
		
	def encrypt(self, keyword, string):
		key_list[1:1] = list(keyword)
		for char in alphabet:
			if char not in key_list:
				key_list.append(char)
		i = 0
		for item in key_list:
			alph_dict[alphabet[i]] = item
			i += 1
		ans = ''
		for letter in string:
			new_letter = alph_dict[letter]
			ans += new_letter
		return ans
		
	def decrypt(self, keyword, string):
		pass