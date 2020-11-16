.text
.globl main

main:
	li $t0,25     #load immediate
	li $t1,10
	sub $t2, $t0, $t1
	li $v0,10     #systemcall no to exit 
	syscall       #system call