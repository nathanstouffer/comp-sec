#!/usr/bin/python3
from scapy.all import *

print("--- SNIFFING TCP PACKETS FROM 10.0.2.5 FOR PORT 23 ---")

def print_pkt(pkt):
    print("Source IP: " + pkt[IP].src)
    print("Destination IP: " + pkt[IP].dst)
    print("Protocal: " + str(pkt[IP].proto))
    print("\n")

pkt = sniff(filter='tcp and dst port 23 and src host 10.0.2.5', prn=print_pkt)
