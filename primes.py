i=1
angles = {}
registeredAngles = []

while(True):
    prime=True
    a=360.0/i
    for j in range(1,i):
        angles[j] = a*j
    for k in angles.values():
        if k in registeredAngles:
            prime = False
            break
    if prime:
        for k in angles.values():
            registeredAngles.append(k)
        print str(i)+"\n"##+"  is     prime\n"
##    else:
##        print str(i)+"  is not prime\n"
    i+=1

