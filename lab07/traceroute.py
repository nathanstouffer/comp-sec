#!/usr/bin/python3
from scapy.all import *

dest = "8.8.8.8" # google

print("\n\n--- RUNNING TRACEROUTE ---")
print("maximum hops: 20")
print("dst = " + dest)
print("")

# create packet
ip   = IP(dst=dest)
icmp = ICMP()

# for loop to run traceroute
for i in range(0, 20):
    ip.ttl = i + 1 		# set ttl value
    pkt = ip/icmp  		# create packet
    
    reply = sr1(pkt, timeout=1, verbose=0)		# send packet, wait for reply
    if (reply != None):
        print("ttl: {0:<3} ip: {1}".format(i+1, reply[IP].src))
    else:
        print("ttl: {0:<3} ip: timed out".format(i+1))
print("")
