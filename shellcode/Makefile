all:
	nasm -f elf32 -o shellcode.o shellcode.asm
	ld -m elf_i386 -o shellcode.bin shellcode.o
	nasm -f elf64 shellcode64.asm -o shellcode64.o
	ld shellcode64.o -o shellcode64.bin
