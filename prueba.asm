section constantes
	cst1 123
	cst2 340
	cst3 abc
section codigo
	mov r01,cst1
	mov r02,r03
	add var1,r02
	sub var2,var3
	mul r05,var1
	div cst1,cst2
	mov cst3,r01
	nop
	not r02
	jmp HOLA
HOLA:
section variables
	var1 1
	var2 1
	var3 5
