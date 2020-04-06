from Crypto.Cipher import AES
from Crypto.Util import Padding

key_hex_string = '00112233445566778899aabbccddeeff'
iv_hex_string  = '000102030405060708090a0b0c0d0e0f'
key = bytes.fromhex(key_hex_string)
iv  = bytes.fromhex(iv_hex_string)
data = b'The quick brown fox jumps over the lazy dog'
print("Length of original data: {0:d}".format(len(data))) # should be 43 bytes
print("Original data: {0}".format(data))

# encrypt the data piece by piece
cipher = AES.new(key, AES.MODE_CBC, iv)
ciphertext  = cipher.encrypt(data[0:32])
ciphertext += cipher.encrypt(Padding.pad(data[32:], 16))
print("Ciphertext: {0}".format(ciphertext.hex()))

# encrypt the entire data


# decrypt the ciphertext
cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = cipher.decrypt(ciphertext)
print("Plaintext: {0}".format(Padding.unpad(plaintext, 16)))
