global _start

mensagem db "hello world",0xA

_start:
	mov eax, "hell"
	push eax
	mov eax, "o wo"
	push eax
	mov eax, "rld "
	push eax
	mov eax, 4
	mov ebx, 1
	mov ecx, esp
	mov edx,12
	int 0x80

	mov eax,1
	mov ebx,0
	int 0x80
