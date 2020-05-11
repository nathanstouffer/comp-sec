#!/usr/bin/python3
from sys import argv

# function to convert input to bytes
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

def repeat(byte, length):
    repeated = str(byte)
    while (len(repeated) < length):
        repeated += str(byte)
    return bytearray(repeated)

def output(head, bytearr):
    out = ''.join(format(x, '02x') for x in bytearr)
    print(head + out)

def foutput(file_name, bytearr):    
    key = ''.join(format(x, '02x') for x in bytearr)
    fout = open(file_name, 'w')
    fout.write(key)
    fout.close

script, first = argv
data = toBytes(first)

byte = bytearray.fromhex("01")
for i in range(1, 255):
    #print(byte)
    seq = repeat(byte, len(str(data)))
    xord = bytearray(x^y for x,y in zip(data, seq))
    if (i == 16):
        #foutput(outfile, xord)
        output(" first: ", data)
        output("second: ", seq)
        output(" final: ", xord)
        print("  byte: " + ''.join(format(x, '02x') for x in byte)  + " xord: " + xord)
    # update byte
    byte[0] += 0x01

