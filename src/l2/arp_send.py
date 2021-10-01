#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from scapy.all import *
from scapy.layers.l2 import ARP, Ether

packet = Ether(dst='ff:ff:ff:ff:ff')/ARP(pdst='10.5.0.3')
packet.show()                               # показать структуру пакета
sendp(packet, iface="eth0")                 # отправить запрос через интерфейс wlp7s0

