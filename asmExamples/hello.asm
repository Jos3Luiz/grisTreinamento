global _start

mensagem db "hello world",0xA

_start:
	mov eax, 4
	mov ebx, 1
	mov ecx, mensagem
	mov edx,12
	int 0x80

	mov eax,1
	mov ebx,0
	int 0x80
