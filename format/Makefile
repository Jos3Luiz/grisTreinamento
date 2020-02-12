all:
	#disable aslr
	echo 0 | sudo tee /proc/sys/kernel/randomize_va_space

	sudo bash -c 'echo 0 > /proc/sys/kernel/randomize_va_space'
	gcc -o format1 format1.c -fno-stack-protector -m32 -z execstack -no-pie
	gcc -o print print.c -fno-stack-protector -z execstack -no-pie
	gcc -o print2 print2.c -fno-stack-protector -z execstack -no-pie
	gcc -o print3 print3.c -fno-stack-protector -z execstack -no-pie
