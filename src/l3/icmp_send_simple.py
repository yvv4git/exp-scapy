#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from scapy.layers.inet import IP, ICMP
from scapy.sendrecv import sr1

packet = IP(dst="10.5.0.3") / ICMP()
packet.show()
answer = sr1(packet)

print(answer.summary())
answer.show()
