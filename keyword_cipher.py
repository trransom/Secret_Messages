# Keyword cipher
from ciphers import Cipher
import string

alphabet = string.ascii_lowercase
key_list = []
encrypt_dict = {}
decrypt_dict = {}

def clearDict(dictionary):
	dictionary.clear()

#Make constructor handle overridden keyword, define 
#your own keyword.
class Keyword(Cipher):
	
	def __init__(self):
		pass
		
	def encrypt(self, keyword, string):
		key_list.clear()
		clearDict(encrypt_dict)
		key_list[1:1] = list(keyword)
		for char in alphabet:
			if char not in key_list:
				key_list.append(char)
		i = 0
		for item in key_list:
			encrypt_dict[alphabet[i]] = item
			i += 1
		ans = ''
		for letter in string:
			new_letter = encrypt_dict[letter]
			ans += new_letter
		return ans
		
	def decrypt(self, keyword, string):
		key_list.clear()
		clearDict(decrypt_dict)
		key_list[1:1] = list(keyword)
		for char in alphabet:
			if char not in key_list:
				key_list.append(char)
		i = 0
		for item in key_list:
			if i <= 25:
				decrypt_dict[key_list[i]] = alphabet[i]
				i += 1
		ans = ''
		for letter in string:
			new_letter = decrypt_dict[letter]
			ans += new_letter
		return ans
		