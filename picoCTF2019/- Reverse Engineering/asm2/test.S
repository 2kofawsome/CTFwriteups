asm2:
	<+0>:	push   ebp #4, 40
	<+1>:	mov    ebp,esp
	<+3>:	sub    esp,0x10 #-16
	<+6>:	mov    eax,DWORD PTR [ebp+0xc] #40 to eax
	<+9>:	mov    DWORD PTR [ebp-0x4],eax #40 to 0x4
	<+12>:	mov    eax,DWORD PTR [ebp+0x8] #4 to eax
	<+15>:	mov    DWORD PTR [ebp-0x8],eax #4 to 0x8
	<+18>:	jmp    0x50c <asm2+31>
	<+20>:	add    DWORD PTR [ebp-0x4],0x1
	<+24>:	add    DWORD PTR [ebp-0x8],0xbd
	<+31>:	cmp    DWORD PTR [ebp-0x8],0x4933 #<
	<+38>:	jle    0x501 <asm2+20>
	<+40>:	mov    eax,DWORD PTR [ebp-0x4]
	<+43>:	leave  
	<+44>:	ret    

