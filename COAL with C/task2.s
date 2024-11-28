	.file	"task2.c"
	.text
	.globl	_example2_switch
	.def	_example2_switch;	.scl	2;	.type	32;	.endef
_example2_switch:
LFB10:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	subl	$16, %esp
	movl	8(%ebp), %eax
	movl	%eax, -4(%ebp)
	movl	12(%ebp), %eax
	subl	$100, %eax
	cmpl	$6, %eax
	ja	L2
	movl	L4(,%eax,4), %eax
	jmp	*%eax
	.section .rdata,"dr"
	.align 4
L4:
	.long	L3
	.long	L2
	.long	L5
	.long	L6
	.long	L7
	.long	L2
	.long	L7
	.text
L3:
	movl	-4(%ebp), %edx
	movl	%edx, %eax
	addl	%eax, %eax
	addl	%edx, %eax
	sall	$2, %eax
	addl	%edx, %eax
	movl	%eax, -4(%ebp)
	jmp	L8
L5:
	addl	$10, -4(%ebp)
L6:
	addl	$11, -4(%ebp)
	jmp	L8
L7:
	movl	-4(%ebp), %eax
	imull	-4(%ebp), %eax
	movl	%eax, -4(%ebp)
	jmp	L8
L2:
	movl	$0, -4(%ebp)
L8:
	movl	16(%ebp), %eax
	movl	-4(%ebp), %edx
	movl	%edx, (%eax)
	nop
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE10:
	.globl	_max_switch
	.def	_max_switch;	.scl	2;	.type	32;	.endef
_max_switch:
LFB11:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	subl	$16, %esp
	movl	8(%ebp), %eax
	cmpl	12(%ebp), %eax
	jle	L10
	movl	8(%ebp), %eax
	cmpl	16(%ebp), %eax
	jl	L10
	movl	8(%ebp), %eax
	movl	%eax, -4(%ebp)
	jmp	L11
L10:
	movl	12(%ebp), %eax
	cmpl	8(%ebp), %eax
	jl	L12
	movl	12(%ebp), %eax
	cmpl	16(%ebp), %eax
	jl	L12
	movl	12(%ebp), %eax
	movl	%eax, -4(%ebp)
	jmp	L11
L12:
	movl	16(%ebp), %eax
	movl	%eax, -4(%ebp)
L11:
	movl	20(%ebp), %eax
	cmpl	$2, %eax
	je	L14
	cmpl	$2, %eax
	jg	L15
	testl	%eax, %eax
	js	L13
	jmp	L20
L15:
	cmpl	$3, %eax
	je	L17
	jmp	L13
L20:
	addl	$1, -4(%ebp)
	jmp	L18
L14:
	addl	$2, -4(%ebp)
	jmp	L18
L17:
	addl	$3, -4(%ebp)
	jmp	L18
L13:
	movl	-4(%ebp), %eax
	addl	%eax, %eax
	movl	%eax, -4(%ebp)
L18:
	movl	-4(%ebp), %eax
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE11:
	.ident	"GCC: (MinGW.org GCC-6.3.0-1) 6.3.0"
