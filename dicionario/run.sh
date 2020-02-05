#!/bin/bash

echo -n "" > senhas.txt 

senhas=(flamengo123  coisa1  senha12  fish)

for i in "${senhas[@]}"; do

	hashmd5=$(echo -n $i | md5sum | cut  -b 1-32)
	echo $i=$hashmd5
	echo $hashmd5 >> senhas.txt
done 


john --format=Raw-MD5 ./senhas.txt
#john  --format=Raw-MD5 ./senhas.txt --wordlist=/usr/share/wordlists/rockyou.txt
john --show --format=Raw-MD5 senhas.txt
