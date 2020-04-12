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

def output(head, bytearr):
    out = ''.join(format(x, '02x') for x in bytearr)
    print(head + out)

def foutput(file_name, bytearr):    
    key = ''.join(format(x, '02x') for x in bytearr)
    fout = open(file_name, 'w')
    fout.write(key)
    fout.close()

script, outfile, first, second = argv
aa = toBytes(first)
bb = toBytes(second)
xord = bytearray(x^y for x,y in zip(aa, bb))
foutput(outfile, xord)
output(" first: ", aa)
output("second: ", bb)
output(" final: ", xord)
