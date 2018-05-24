# Keyword cipher
from ciphers import Cipher
import string

alphabet = string.ascii_lowercase + ' '


'''
	Encrypts or decrypts the passed in string depending on the boolean value given.
'''
def dencrypt(keyword, dictionary, key_list, bool):

	dictionary.clear()
	key_list.clear()
	dictionary[' '] = ' '

	#Add the new keyword to the key list
	key_list[1:1] = list(keyword)
	
	#Create the rest of the alphabet, and append it to the keylist.
	alph = [char for char in alphabet if char not in key_list]
	key_list.extend(alph)
	
	if bool==1:
		dictionary.update({alph_letter: code_letter for alph_letter, code_letter in zip(alphabet, key_list)})
		return dictionary
	elif bool==0:
		dictionary.update({code_letter: alph_letter for code_letter, alph_letter in zip(key_list, alphabet)})
		return dictionary
#		ans_string = [dictionary[char] for char in string]
#		ans = ''.join(ans_string)
#		return ans
#	elif bool==0:
#		dictionary.update({code_letter: alph_letter for code_letter, alph_letter in zip(key_list, alphabet)})
#		ans_string = [dictionary[char] for char in string]
#		ans = ''.join(ans_string)
#		return ans

class Keyword(Cipher):


#	key_list = []
#	start_dict = {}
#	encrypt_dict = dencrypt(keyword, start_dict, key_list, 1)
#	decrypt_dict = dencrypt(keyword, start_dict, key_list, 0)
	
	
	'''
		Allows the user to initialize the class by passing in their own keyword for the cipher.
	'''
	def __init__(self, keyword='kryptos', key_list=[], start_dict={}):
		self.keyword = keyword
		self.key_list = key_list
		self.start_dict = start_dict
		self.encrypt_dict = dencrypt(self.keyword, self.start_dict, self.key_list, 1)
		self.decrypt_dict = dencrypt(self.keyword, self.start_dict, self.key_list, 0)
		super().__init__(self.encrypt_dict, self.decrypt_dict)
		
	'''
		Encrypts the given string by calling 'dencrypt' with a boolean value of 1
		and by passing in the encrypt_dict as the dictionary argument.
	'''
#	def encrypt(self, keyword, string):
#		return dencrypt(self.keyword, self.encrypt_dict, self.key_list, 1)
		
	'''
		Encrypts the given string by calling 'dencrypt' with a boolean value of 0
		and by passing in the decrypt_dict as the dictionary argument.
	'''
#	def decrypt(self, keyword, string):
#		return dencrypt(self.keyword, self.decrypt_dict, self.key_list, 0)
