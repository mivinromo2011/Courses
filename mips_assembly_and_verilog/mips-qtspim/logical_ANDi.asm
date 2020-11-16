.text
.globl main

main:
	li $t0,1     #load immediate
	andi $t2, $t0, 3
	li $v0,10     #systemcall no to exit 
	syscall       #system call