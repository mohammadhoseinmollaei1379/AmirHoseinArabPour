; MOV

org 100h
; mov al, 45h
; mov bh, al
; mov cx, 341fh
; mov dx, cx
; mov bl, dx    : error
; mov al, 74fh  : error 
; mov ax, 6h
; mov ds, 345h  : error
; mov ax, 345h
; mov ds, ax
;----------------------
; add
; mov al, 35h
; mov bl, 26h
; add al, bl 
; mov al, 35h
; add al, 26h
; mov al, 0ffh  ;   1111 1111
; add al, 1h    ; 1 0000 0000
; mov ah, 25h   ;   0010 0101
; add ah, 0afh  ;   1010 1111
                ;   1101 0100  
;----------------------
; stack  ss:sp   cs:ip
; mov  ax, 12e4h
; push ax

; mov  di, 7f52h
; push di

; pop  cx 

; mov  al, 12h
; push al      ; error
; mov  dl, [1000]; ds:1000 
;----------------------
; a db 01000001b
; b dw 0100000101100001b
; c dw 1a52h 
;----------------------
a db 2 dup(1fh)         ; a db 1fh, 1fh

b db 3 dup(?)

c equ 35                ; const in C & equ in ASM