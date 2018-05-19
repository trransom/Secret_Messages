#One Time Pad
from ciphers import Cipher

class Pad(ciphers):

	num_dict = {number: letter for letter, number in zip('abcdefghijklmnopqrstuvwxyz', range(0,27))}
	pad = '12345'
	
	def __init__(self, pad='12345'):
		self.pad = pad

	def encrypt(self, string):
		
		
	def decrypt(self, string):
		pass