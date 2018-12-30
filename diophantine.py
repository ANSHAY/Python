#diophantine equation:  6a+9b+20c=n

n=int(input('enter number of McNuggets to buy'))
impossibleComb=0
count=0
flag=0
c=0
##while count < 6:
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
