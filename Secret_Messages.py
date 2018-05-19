#Secret Messages
from atbash_cipher import Atbash
from ciphers import Cipher
from keyword_cipher import Keyword
from polybius_cipher import Polybius
import re
import string


repeat = True
keyword = ''
code_list = ['atbash', 'keyword', 'polybius']

def numLetters(s):
	invalidChars = set(string.punctuation)
	isNum = any(i.isdigit() for i in s)
	specChar = any(char in invalidChars for char in s)
	if isNum or specChar:
		return True
'''
	Encrypts the given string depending on whether
	code is equal to 'atbash', 'polybius', or 'keyword'.
'''
def encrypt(code, string):
	if code=='atbash':
		atbash = Atbash()
		return atbash.encrypt(string)
	elif code=='polybius':
		poly = Polybius()
		return poly.encrypt(string)
	elif code=='keyword':
		key = Keyword(keyword)
		return key.encrypt(key.keyword, string)
		
'''
	Decrypts the given string depending on whether
	code is equal to 'atbash', 'polybius', or 'keyword'.
'''
def decrypt(code, string):
	if code=='atbash':
		atbash = Atbash()
		return atbash.decrypt(string)
	elif code=='polybius':
		poly = Polybius()
		return poly.decrypt(string)
	elif code=='keyword':
		key = Keyword(keyword)
		return key.decrypt(key.keyword, string)


print('This is a Secret Messages program. Choose your cipher and encrypt or decrypt your message!\n\n')

while repeat==True:
	print('These are the current ciphers available:\n\n-Atbash\n-Keyword\n-Polybius\n\n')
	code = input("Which cipher would you like to use?\n").lower()
	while code not in code_list:
		print(code + ' is not an available cipher. Please try again.')
		code = input("Which cipher would you like to use?\n").lower()
	if code=='keyword':
		keyword = input('Which keyword would you like to use? (Keywords without repeating letters work best)\n')
		while numLetters(keyword):
			print('Please enter a keyword without any digits or special characters')
			keyword = input('Which cipher would you like to use?\n').lower()
			
	crypt = input("Excellent. Would you like to encrypt or decrypt?\n").lower()
	message = input("What message would you like to {}?\n").format(crypt)
	if code != 'polybius':
		while numLetters(message):
			print('Please enter a message without numbers or special characters.\n')
			message = input('What message would you like to encrypt or decrypt?\n')
	elif code=='polybius':
		if numLetters(message) and crypt != 'decrypt':
			print('Number messages can only be decrypted.\n')
			crypt = 'decrypt'


	if crypt=='encrypt':
		answer = encrypt(code, message)
		print('Your encrypted message is:\n' + answer)
	elif crypt=='decrypt':
		answer = decrypt(code, message)
		print('Your decrypted message is:\n' + answer)

	r = input('\nWould you like to encode or decode another message? y\\n\n')
	if r=='y':
		repeat = True
	else:
		repeat = False
