.globl main
.text
main:
	li $t1,2

	slt $t3, $t1, 1
	li $v0,10
	syscall