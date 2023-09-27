section .bss
    myString resb 6 

section .text
    global _start

_start:

    mov edi, myString  
    mov ecx, 6         
    db 0ebH,0ffH,0c0H,048H ; inc  eax  dec eax
    mov al, 0x73         
    db 0ebH,0ffH,0c0H,048H ; inc  eax  dec eax
    stosb              
    mov al, 0x65         
    stosb
    mov al, 0x63         
    stosb 
    mov al, 0x72         
    stosb 
    mov al, 0x65         
    stosb 
    mov al, 0x74         
    stosb            

    mov eax, 4           
    mov ebx, 1            
    mov ecx, myString     
    mov edx, 6           
    int 0x80             

    mov eax, 1            
    int 0x80              
