section .bss
    myString resb 6 

section .text
    global _start

_start:

    mov edi, myString  
    mov ecx, 6
    db 0xeb
    db 0xff
    db 0xc0
    db 0x48
    db 0x90
    db 0x90         
    mov al, 0x73        
    stosb 
    db 0xeb
    db 0xff
    db 0xc0
    db 0x48
    db 0x90
    db 0x90              
    mov al, 0x65         
    stosb
    db 0xeb
    db 0xff
    db 0xc0
    db 0x48
    db 0x90
    db 0x90 
    mov al, 0x63         
    stosb 
    db 0xeb
    db 0xff
    db 0xc0
    db 0x48
    db 0x90
    db 0x90 
    mov al, 0x72         
    stosb 
    db 0xeb
    db 0xff
    db 0xc0
    db 0x48
    db 0x90
    db 0x90 
    mov al, 0x65         
    stosb 
    db 0xeb
    db 0xff
    db 0xc0
    db 0x48
    db 0x90
    db 0x90 
    mov al, 0x74         
    stosb

	            

    mov eax, 4           
    mov ebx, 1            
    mov ecx, myString     
    mov edx, 6           
    int 0x80             

    mov eax, 1            
    int 0x80              
