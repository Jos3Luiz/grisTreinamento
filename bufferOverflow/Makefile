all:
	gcc -o bufferoverflow bufferoverflow.c -fno-stack-protector -z execstack -O0
	objdump -d -M intel bufferoverflow
