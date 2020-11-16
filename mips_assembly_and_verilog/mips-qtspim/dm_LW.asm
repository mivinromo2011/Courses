.text
.globl main

main:
	li $t0,4     #load immediate
	lw $t2, value
	add $t4,$t0,$t2
	sub $t5,$t0,$t2

	
	li $v0,10     #systemcall no to exit 
	syscall       #system call

	value: .word 20 # assign the some memory for the tag 'value' and value 20 