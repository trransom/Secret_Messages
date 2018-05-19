# Polybius Square Cipher
from ciphers import Cipher
import string

poly_dict = {
	'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15, ' ': ' ',
	'f': 21, 'g': 22, 'h': 23, 'i': 24, 'j': 24, 'k': 25, 
	'l': 31, 'm': 32, 'n': 33, 'o': 34, 'p': 35, 
	'q': 41, 'r': 42, 's': 43, 't': 44, 'u': 45,
	'v': 51, 'w': 52, 'x': 53, 'y': 54, 'z': 55
	}
			
r_poly_dict = {
	'11': 'a', '12': 'b', '13': 'c', '14': 'd', '15': 'e', ' ': ' ',
	'21': 'f', '22': 'g', '23': 'h', '24': '(i\j)', '25': 'k',
	'31': 'l', '32': 'm', '33': 'n', '34': 'o', '35': 'p', 
	'41': 'q', '42': 'r', '43': 's', '44': 't', '45': 'u', 
	'51': 'v', '52': 'w', '53': 'x', '54': 'y', '55': 'z'
	}
				
				
class Polybius(Cipher):
	num_list = [
		11, 12, 13, 14, 15, 
		21, 22, 23, 24, 25,
		31, 32, 33, 34, 35, 
		41, 42, 43, 44, 45, 
		51, 52, 53, 54, 55
		]
		
	'''
		Encrypts the given string by turning it to lowercase and then running it against
		the poly_dict dictionary.
	'''
	def encrypt(self, string):
		ans = ''
		s = string.lower()
		for char in s:
			new_char = poly_dict[char]
			ans += str(new_char) + ' '
		return ans
	
	'''
		Decrypts the given string by splitting it on spaces and then running it against
		the r_poly_dict dictionary.
	'''
	def decrypt(self, string):
		ans = ''
		code = string.split(' ')
		for num in code:
			new_num = r_poly_dict[num]
			ans += str(new_num)
		return ans
