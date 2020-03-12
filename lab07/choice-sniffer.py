#!/usr/bin/python3
from scapy.all import *

print("--- SNIFFING TCP PACKETS for 110.0.26.8/14 ---")

def print_pkt(pkt):
    print("Source IP: " + pkt[IP].src)
    print("Destination IP: " + pkt[IP].dst)
    print("Protocal: " + str(pkt[IP].proto))
    print("\n")

pkt = sniff(filter='dst port 14 and dst host 110.0.26.8', prn=print_pkt)
