all:
	#disable aslr
	echo 0 | sudo tee /proc/sys/kernel/randomize_va_space
	gcc -o bufferoverflow bufferoverflow.c -fno-stack-protector -z execstack -O0
	#objdump -d -M intel bufferoverflow
