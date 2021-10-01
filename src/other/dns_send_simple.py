#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from scapy.layers.dns import DNS, DNSQR
from scapy.layers.inet import IP, UDP
from scapy.sendrecv import sr1

# Спросим у google dns - какой ip адрес у сайта karuna.group
dns_req = IP(dst='8.8.8.8') / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qname='karuna.group'))
answer = sr1(dns_req, verbose=0)

# print(answer[DNS].summary())          # когда нужен только ip
answer.show()         # можно детальней рассмотреть ответ dns сервера
