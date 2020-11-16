.text
.globl main

main:
	li $t0,1     #load immediate
	li $t1,3
	and $t2, $t0, $t1
	li $v0,10     #systemcall no to exit 
	syscall       #system call