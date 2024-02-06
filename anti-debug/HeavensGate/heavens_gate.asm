format ELF executable
segment readable executable

SYS_EXIT_64BIT=60

entry $

    jmp 0x33:start64 

start64:
use64

    mov eax, 1      
    mov edi, 1      
    mov esi, msg2   
    mov edx, msgLen2        
    db 0x0F 
    db 0x05  ; syscall

    db 0x48
    db 0xB8
    db 0xFA
    db 0xFA  ; mov rax, qword 0xf4fa48b8fafafafa
    db 0xFA  
    db 0xFA
    db 0x48
    db 0xB8
    db 0xFA
    db 0xF4

    mov eax, 'Z'
    mov eax, 'A'
    mov eax, 'Y'
    mov eax, 'O'
    mov eax, 'T'
    mov eax, 'E'
    mov eax, 'M'
    mov eax, '{'
    mov eax, 'H'
    mov eax, '3'
    mov eax, 'A'
    mov eax, 'V'
    mov eax, '3'
    mov eax, 'N'
    mov eax, 'S'
    mov eax, '_'
    mov eax, 'G'
    mov eax, 'A'
    mov eax, 'T'
    mov eax, '3'
    mov eax, '}'

    xor rdi,rdi
    mov eax, SYS_EXIT_64BIT
    syscall
    ud2


msg2:
    db "Where is the secret message???"
msgLen2 = $-msg2