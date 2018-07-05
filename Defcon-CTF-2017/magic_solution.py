import r2pipe, binascii, os

def printcode(pw): 
    pw = binascii.unhexlify(pw)
    with open("codes", "ab") as fil:
            fil.write(pw)
            fil.close()

def hexvalue(addr):
    pw = []
    a = r2.cmdj("pdj 1 @{}".format(addr))[0]
    pw.append(a['opcode'])
    b = pw[0].split(',')[1]
    b = str(b)[3:5]
    printcode(b)
    
def getaddr():
    i = 48
    i2 = 60
    s = []
    c = r2.cmd("pdf~call fcn")
    while i2 <= len(c):
        addr = c[i:i2]
        hexvalue(addr)
        i=i+61
        i2=i2+61
    with open("codes", "a") as fil:
        fil.write("\n")
        fil.close()


files = sorted(os.listdir("/home/jl/shared/CTFs/defcon2017/2magic/magic_dist/"))

for i in files:
    if i != "answer" and i != "findcode.py" and i != "codes":
        r2 = r2pipe.open("./{}".format(i))
        r2.cmd("aaa")
        m = r2.cmd("afl~fcn")
        mn = m[-83:-73]
        r2.cmd("s {}".format(mn))
        with open("codes", "a") as fil:
            fil.write("-> "+str(i)+": \n")
            fil.close()
        getaddr()
    else:
        pass
