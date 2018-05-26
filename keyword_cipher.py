# Keyword cipher
from ciphers import Cipher
import string

alphabet = string.ascii_lowercase + ' '



def dencrypt(keyword, dictionary, key_list, bool):
	'''
	Encrypts or decrypts the passed in string depending on the boolean value given.
	'''
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

class Keyword(Cipher):

	
	def __init__(self, keyword='kryptos', key_list=[], start_dict={}):
		'''
		Allows the user to initialize the class by passing in their own keyword for the cipher.
		'''
		self.keyword = keyword
		self.key_list = key_list
		self.start_dict = start_dict
		self.encrypt_dict = dencrypt(self.keyword, self.start_dict, self.key_list, 1)
		dkey_list = []
		dstart_dict = {}
		self.decrypt_dict = dencrypt(self.keyword, dstart_dict, dkey_list, 0)
		super().__init__('placeholder', self.encrypt_dict, self.decrypt_dict)
