# Keyword cipher
from ciphers import Cipher
import string

alphabet = string.ascii_lowercase
key_list = []
encrypt_dict = {}
decrypt_dict = {}

#Empties the dictionary given as an argument
def clear(dictionary, list):
	dictionary.clear()
	list.clear()

#Make constructor handle overridden keyword, define 
#your own keyword.
class Keyword(Cipher):
	
	def __init__(self):
		pass
		
	def encrypt(self, keyword, string):
		#clear the encryption dictionary and the keyword list
		clear(encrypt_dict, key_list)
		
		#Add the new keyword to the key list
		key_list[1:1] = list(keyword)
		
		#Create the rest of the alphabet, and append it to the keylist.
		alph = [char for char in alphabet if char not in key_list]
		key_list.extend(alph)
		
		#Create the encryption dictionary
		encrypt_dict.update({alph_letter: code_letter for alph_letter, code_letter in zip(alphabet, key_list)})
		
		#Create the answer string
		ans_string = [encrypt_dict[char] for char in string]
		ans = ''.join(ans_string)
		return ans
		
	def decrypt(self, keyword, string):
		clear(decrypt_dict, key_list)
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
		