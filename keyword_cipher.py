# Keyword cipher
from ciphers import Cipher
import string

alphabet = string.ascii_lowercase




#Empties the dictionary given as an argument
def clear(dictionary, list):
	dictionary.clear()
	list.clear()
	
def dencrypt(keyword, string, dictionary, key_list, bool):
	#Add the new keyword to the key list
	key_list[1:1] = list(keyword)
	
	#Create the rest of the alphabet, and append it to the keylist.
	alph = [char for char in alphabet if char not in key_list]
	key_list.extend(alph)
	
	if bool==1:
		dictionary.update({alph_letter: code_letter for alph_letter, code_letter in zip(alphabet, key_list)})
		ans_string = [dictionary[char] for char in string]
		ans = ''.join(ans_string)
		return ans
	elif bool==0:
		dictionary.update({code_letter: alph_letter for code_letter, alph_letter in zip(key_list, alphabet)})
		ans_string = [dictionary[char] for char in string]
		ans = ''.join(ans_string)
		return ans
		
#Make constructor handle overridden keyword, define 
#your own keyword.
class Keyword(Cipher):

	keyword = 'kryptos'
	encrypt_dict = {}
	decrypt_dict = {}
	key_list = []
	
	def __init__(self, keyword='kryptos', encrypt_dict={}, decrypt_dict={}, key_list=[]):
		self.keyword = keyword
		self.encrypt_dict = encrypt_dict
		self.decrypt_dict = decrypt_dict
		self.key_list = key_list
		
	def encrypt(self, keyword, string):
		clear(self.encrypt_dict, self.key_list)
		return dencrypt(self.keyword, string, self.encrypt_dict, self.key_list, 1)
		
	def decrypt(self, keyword, string):
		clear(self.decrypt_dict, self.key_list)
		return dencrypt(self.keyword, string, self.decrypt_dict, self.key_list, 0)
		