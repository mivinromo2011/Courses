.text
.globl main

main:
	li $t0,4     #load immediate
	li $t1,0x10010000 #the address
	lw $t3, value
	add $t4,$t3,$t0
	sub $t5,$t3,$t0
	sw $t5, 0($t1)

	
	li $v0,10     #systemcall no to exit 
	syscall       #system call

	value: .word 20 # assign the some memory for the tag 'value' and value 20 