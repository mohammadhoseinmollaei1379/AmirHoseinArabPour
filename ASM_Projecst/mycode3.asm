;SUB

;MOV AL,4EH

;MOV AH, 12H

;SUB AL, AH

;SBB  
;--------------------
;MUL   BYTE * BYTE
;.model small
;--------------------
;.stack 32
;--------------------
;.data
;    N1 DB 1FH
;    N2 DB 3AH
;    R  DW  ?
;--------------------
;.code
;MAIN:
;        MOV AX, @data
;        MOV DS, AX
;        
;        MOV AX, 00
;        
;        MOV AL, N1     ;»«Ìœ œ— À»«  AL »«‘œ
;        MUL N2         ; AX = AL * N2
;        
;        MOV R, AX
;        
;        END MAIN
;
;END code
;
;MUL  WORD * WORD
;.model small
;--------------------
;.stack 32
;--------------------
;.data
;    N1 DW 12F4H
;    N2 DW 3E21H
;    R  DW 2 DUP(?)
;--------------------
;.code
;MAIN:
;        MOV AX, @data
;        MOV DS, AX
;        
;        MOV AX, 00
;       
;        MOV AX, N1     ; çÊ‰ WORD Œ” Â »«Ìœ »—Ì“Ì„  ÊÌ AX
;        MUL N2         ; DX:AX
;        
;        MOV R, AX
;        MOV R+2, DX
;        
;        END MAIN
;
;END code
;--------------------
;.model small
;--------------------
;.stack 32
;--------------------
;.data
;    N1 DB 23
;    N2 DB 5
;--------------------
;.code
;MAIN:
;        MOV AX, @data
;        MOV DS, AX
;        
;        MOV AL, N1     
;        
;        SUB AH, AH         
;        
;        ;MOV BL, N2       ¬œ—” œÂÌ À»« Ì
;        DIV BL          ;AL = 4, AH = 3
;        
;        END MAIN 
;DIV  WORD / WORD
;MOV  AX, 20034
;SUB  DX, DX
;MOV  BX, 200
;DIV  BX
;AX
;DX
;END code

; AND
; X     Y       AND
; 0     0        0
; 0     1        0
; 1     0        0
; 1     1        1

;MOV BL, 11110100B
;AND BL, 01100001B
;        01100000
;C = 0
;O = 0

;S = 0
;Z = 0
;P = 1
;AND AH, AH  ; ZF = 1
;JZ ...

; OR
; X     Y       OR
; 0     0        0
; 0     1        1
; 1     0        1
; 1     1        1 
;MOV BL, 11110100B
;OR  BL, 01100001B
;       11110101

; XOR
; X     Y       XOR
; 0     0        0
; 0     1        1
; 1     0        1
; 1     1        0 

;MOV BL, 11110100B
;XOR BL, 01100001B  
;       10010101

;XOR  AH, AH  ; AH = 0

;XOR  AX, BX  ; ZF = 1 ;«ê— œÊ À»«  »« Â„ »—«»— »«‘‰œ Õ«’· 0 ŒÊ«Âœ ‘œ 

;XOR  BL, 04H  ; 0000 0100    ; „⁄òÊ” „Ì ò‰œ Ìò »Ì  „⁄Ì‰ —« 

; SHR, SHL

;MOV AL, 11111111B
;SHR AL, 1          ; 011111111   ,  CF = 1  

;MOV BX, 0FFFFH
;MOV CL, 2
;SHR BX, CL         ;0111111111111111 CF = 1

;MOV DL, 11111111B
;SHL DL, 1          ; 111111110   ,  CF = 1  

;ROR RIGHT, ROL LEFT

MOV BL, 11111110B
;ROR BL, 1           ;01111111 , CF = 0
;ROR BL, 1           ;10111111 , CF = 1

;MOV CL, 2
;ROR BL, CL
;ROR BL, 2

ROL BL, 1           ;11111101 , CF = 1