# Atbash Cipher
from ciphers import Cipher
from collections import OrderedDict

class Atbash(Cipher):
#    backwards = {number: letter for letter, number in zip('abcdefghijklmnopqrstuvwxyz'[::-1], range(1, 27))}
#	forwards = {number: letter for letter, number in zip('abcdefghijklmnopqrstuvwxyz', range(1, 27))}
	forwards = OrderedDict(zip(string.ascii_lowercase, string.ascii_lowercase[::-1]))
	backwards = OrderedDict(zip(string.ascii_lowercase[::-1], range(1, 27)))

    def __init__(self, string):
        pass

    def encrypt(self, string):
		ans = ''
        for char in string:
			int = backwards[char]
			

    def decrypt(self, text):
        pass
