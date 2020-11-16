.text
.globl main

main:
	li $t0,4     #load immediate
	srl $t2, $t0, 2
	li $v0,10     #systemcall no to exit 
	syscall       #system call