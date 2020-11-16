.text
.globl main

main:
	li $t0,25     #load immediate
	li $t1,10
	mult $t1, $t0
	li $v0,10     #systemcall no to exit 
	syscall       #system call