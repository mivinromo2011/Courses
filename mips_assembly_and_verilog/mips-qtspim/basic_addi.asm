.text
.globl main

main:
	li $t0,25     #load immediate
	add $t2, $t0, 10
	li $v0,10     #systemcall no to exit 
	syscall       #system call