getBin = lambda x: x >= 0 and str(bin(x))[2:] or "-" + str(bin(x))[3:]

def inp():
    inAdd = input("enter file address:\n")
    outAdd = input("enter destination address:\n")
    compress(inAdd,outAdd)

def compress(inAdd,outAdd):
    iFile = open(inAdd,'r')
    mFile = open('temp','w')
    oFile = open(outAdd,'w')
    iFile.seek(0,0)
    for b in iFile.read():
        print b
        mFile.write(int(b))

    b = mFile.read(1)
    while ~mFile.eof():
        for i in range(0,255):
            if i==b:
                oFile.write(1)
                b = mFile.read(1)
            else:
                oFile.write(0)
    iFile.close()
    mFile.close()
    oFile.close()
            
inp()
