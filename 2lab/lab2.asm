format PE

section '.text' code readable executable

entry start
start:

        mov esi, array
        mov ecx, 0
        mov eax, 0
        mov ebx, 0

        cycle:
                lodsb
                test al, 10001000b
                jnz continue
                add ebx, 1
        continue:
                add ecx, 1
                cmp ecx, 10
                jne cycle

exit:
        ret
        

section '.data' data writeable

array db 10000000b, 00001000b, 00000000b, 00000000b, 00000000b, 00000000b, 00000000b, 00000000b, 00000000b, 10001000b

