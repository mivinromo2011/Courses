.text
.globl main

main:
	li $v0,4
	la $a0,msg1
	syscall

	li $v0,5   #read_int syscall no 5
	syscall
	move $t0,$v0 #moving user input to temporary register

	li $v0,4
	la $a0,msg2
	syscall

	li $v0,5
	syscall
	move $t1,$v0

	add $t2, $t1, $t0

	li $v0,4
	la $a0,msg3
	syscall

	li $v0,1		#print_int syscall value
	move $a0,$t2	#move the sum into a0 for printing
	syscall

	li $v0,10
	syscall

.data

msg1: .asciiz "Enter A:  "
msg2: .asciiz "Enter B:  "
msg3: .asciiz "The Sum is: "
newline: .asciiz "\n" 

