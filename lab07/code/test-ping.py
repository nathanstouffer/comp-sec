#!/usr/bin/python3
from scapy.all import *

dest = "153.90.20.211"	# random ip address

print("--- PINGING ---")
print("dst = " + dest)

ip   = IP(dst=dest)
icmp = ICMP(type='echo-request')

pkt = ip/icmp
print("--- SENT PING ---")
reply = sr1(pkt, timeout=3, verbose=0)

if (reply != None):
    print(dest + " is awake!")
else:
    print(dest + " is not awake")
