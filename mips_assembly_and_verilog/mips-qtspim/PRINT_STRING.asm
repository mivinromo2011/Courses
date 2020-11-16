.text
.globl main

main:
	li $v0,4 #Print_String Syscall
	la $a0,msg #pointer to the string is loaded 
	syscall
	li $v0,10
	syscall

.data

msg: .asciiz "Mithun Github!\n"