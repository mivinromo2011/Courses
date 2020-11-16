#if sum>count => count/sum else: count+sum
.data

.text
.globl main

main:
	li $t0,2
	li $t1,4

	bgt $t0,$t1,division
	add $t0, $t0, $t1
	division:
	    div $t0, $t1
	exit:
	    li $v0,10
	    syscall