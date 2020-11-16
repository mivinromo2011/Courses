.globl main
.text
main:
	li $t1,2
	li $t2,3

	slt $t3, $t1, $t2

	li $v0,10
	syscall