#ADD 1 till reaching 11

.data

.text
.globl main

main:
	li $t0,1
	li $t1,10

while:	beq $t0,11,exit
		
    	addi $t0, $t0, 1
    	j while 
	exit:
	    li $v0,10
	    syscall