#!/usr/bin/python3
from scapy.all import *

def spoof(rcvd):
    if (ICMP in rcvd and rcvd[ICMP].type == 8):
        ip   = IP(src=rcvd[IP].dst, dst=rcvd[IP].src)
        icmp = ICMP(type=0, id=rcvd[ICMP].id, seq=rcvd[IP].seq)
        
	resp = ip/icmp
        send(resp, verbose=0)
        print("sent response")

print("\n--- SPOOFING ICMP echo requests ---")

rcvd = sniff(filter='icmp', prn=spoof)
