#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from scapy.layers.inet import IP, ICMP

# Давайте посмотрим на структуру icmp пакета
packet = IP(dst="nmap.org") / ICMP()
packet.show()
