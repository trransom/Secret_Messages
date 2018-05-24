#Secret Messages
from atbash_cipher import Atbash
from ciphers import Cipher
from keyword_cipher import Keyword
from polybius_cipher import Polybius
import string


repeat = True
keyword = ''
code_list = ['atbash', 'keyword', 'polybius']

'''
	Prints the available ciphers and takes input from the user.
	If the requested cipher is not in the list, the function continues
	to prompt the user.
'''
def begin():
	print('These are the current ciphers available:\n\n-Atbash\n-Keyword\n-Polybius\n\n')
	code = input("Which cipher would you like to use?\n").lower()
	while code not in code_list:
		print(code + ' is not an available cipher. Please try again.')
		code = input("Which cipher would you like to use?\n").lower()
	
	return code

'''
	If polybius is entered as the encryption, the main body of 
	the script calls this function to handle the possible error 
	logic of asking the user for correct input associated with the
	polybius cipher.
'''
def polybius(crypt_arg, message):
	if crypt_arg=='encrypt':
		while numLetters(message):
			print('Only messages without numbers and special characters can be encrypted')
			message = input('What message would you like to %s?\n' % crypt_arg)
	elif crypt_arg=='decrypt':
		bool = True
		poly = Polybius()
		test = message.split(' ')
		#Loops continually, reseting the 'test' string until correct input is given.
		while bool:
			for item in test:
				#If the item in test isn't a digit, prompt for new input.
				if item.isdigit()==False:
					print('Only digits between 11 and 56 can be tested with a single space between every number.\n')
					message = input('What message would you like to %s?\n' % crypt_arg)
					test = message.split(' ')
					continue
				#If the item in test isn't in num_list, prompt for new input.
				if int(item) not in poly.num_list:
					print('Only digits between 11 and 56 can be tested with a single space between every number.\n')
					message = input('What message would you like to %s?\n' % crypt_arg)
					test = message.split(' ')
					break
				#If you've passed both tests and are at the end of the list,
				#you've reached the end of the message without errors. 
				elif item == test[-1]:
					bool = False
					continue
				else:
					continue
	return message

'''
	Returns true if the string contains any numbers 
	or special characters.
'''
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
		return key.encrypt(string)
		
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
		return key.decrypt(string)


print('This is a Secret Messages program. Choose your cipher and encrypt or decrypt your message!\n\n')

while repeat==True:
	code = begin()
	
	#input the keyword if cipher is Keyword
	if code=='keyword':
		keyword = input('Which keyword would you like to use? (Keywords without repeating letters work best)\n')
		while numLetters(keyword):
			print('Please enter a keyword without any digits or special characters')
			keyword = input('Which keyword would you like to use?\n').lower()
			
	#Prompt for 'encrypt' or 'decrypt'. Continue to prompt until either answers have been given.
	crypt = input("Excellent. Would you like to encrypt or decrypt?\n").lower()
	while crypt != 'encrypt' and crypt != 'decrypt':
		crypt = input('Please enter either \'encrypt\' or \'decrypt\'\n')
		
	#Prompt for message. If the cipher is Polybius, run the polybius() function
	#to solve for possible logic errors associated with the Polybius cipher.
	message = input("What message would you like to %s?\n" % crypt)
	if code != 'polybius':
		while numLetters(message):
			print('Please enter a message without numbers or special characters.\n')
			message = input('What message would you like to %s?\n' % crypt)
	elif code=='polybius':
		message = polybius(crypt, message)

	#Call encrypt or decrypt with the correct cipher and the message for encoding/decoding.
	if crypt=='encrypt':
		answer = encrypt(code, message)
		print('Your encrypted message is:\n' + answer)
	elif crypt=='decrypt':
		answer = decrypt(code, message)
		print('Your decrypted message is:\n' + answer)

	#Continue or discontinue the program depending on the input from the user.
	r = input('\nWould you like to encode or decode another message? y\\n\n')
	if r=='y':
		repeat = True
	else:
		repeat = False
