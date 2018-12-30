# ps1

flag=0
c=0
##while count < 6:
for n in range(50,56):
    print('for n= ',n)
    c=0
    while 20*c<=n and n>0:
        b=0
        while 9*b<=n:
            a=0
            while 6*a<=n:
                if (6*a+9*b+20*c)==n:
                    print('possible in packets-',a,'of 6, ',b,'of 9, and ',c,'of 20')
                    flag=1
                    break
                else:
                    a+=1
            b+=1
        c+=1
##print('out of loops')
if flag==0:
    print('no possible combination')
