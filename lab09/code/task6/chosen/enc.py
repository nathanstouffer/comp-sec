#!/usr/bin/python3

from Crypto.Cipher import AES
from Crypto.Util import Padding
from sys import argv


def toBytes(file_name):
    fin = open(file_name)
    line = fin.readline()
    fin.close()
    try:
	# attempt to convert from hex
        return bytearray.fromhex(line)
    except:
        # assume input is a string
        return bytearray(line)

def output(fin, bytearr):
    file_name = fin[:1] + "-out.bin"
    fout = open(file_name, 'w')
    fout.write(bytearr)
    fout.close()

script, file_name = argv

key_hex_string = '00112233445566778899AABBCCDDEEFF'
iv_hex_string  = '31323334353637383930313233343537'
key = bytearray.fromhex(key_hex_string)
iv  = bytearray.fromhex(iv_hex_string)
data = toBytes(file_name)

# Encrypt the entire data
cipher = AES.new(key, AES.MODE_CBC, iv)                   
ciphertext = cipher.encrypt(Padding.pad(data, 16))       
output(file_name, ciphertext)
