#!/usr/bin/python3

from Crypto.Cipher import AES
from Crypto.Util import Padding

def decrypt(ciphertext, key, iv):
    # Decrypt the ciphertext
    cipher = AES.new(key, AES.MODE_CBC, iv)                 
    return cipher.decrypt(ciphertext)

def constructKey(word):
    key_guess = word
    length = len(key_guess)
    # add # symbol
    for i in range(length, 16):
	key_guess += b'#'
    return bytearray(key_guess)

def main():
    # given plain text
    plaintext = "This is a top secret."
    # we know the iv
    iv_hex_string  = 'aabbccddeeff00998877665544332211'
    iv = bytearray.fromhex(iv_hex_string)
    # ciphertext
    ciphertext = bytearray.fromhex("1e479ff8738e2dc5612c00e92782ea811231cbad8a6a9f9f52ff9c9148b9956a")

    # take in file
    fin = open("words.txt")

    key = ''
    decrypted = ''
    for line in fin:
        key_guess = constructKey(line[:-1])
	#print(key_guess)
        if (len(key_guess) == 16):
	    dec_guess = decrypt(ciphertext, key_guess, iv)[0:len(plaintext)]
            #print(dec_guess)
	    if (plaintext == dec_guess):
	        key = key_guess
	        decrypted = dec_guess

    print("The key is: " + key)
    print("The decrypted message is: " + decrypted)
    
    # close the file
    fin.close

main()
