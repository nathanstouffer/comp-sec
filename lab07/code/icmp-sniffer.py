#!/usr/bin/python3
from scapy.all import *

print("--- SNIFFING ICMP PACKETS ---")

def print_pkt(pkt):
    print("Source IP: " + pkt[IP].src)
    print("Destination IP: " + pkt[IP].dst)
    print("Protocal: " + str(pkt[IP].proto))
    print("\n")

pkt = sniff(filter='icmp', prn=print_pkt)
