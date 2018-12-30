# ps2c

largestImpossibleComb=0
count=0
n=6
while count < 6:
    flag=0
    c=0
    while 20*c<=n:
        b=0
        while 9*b<=n:
            a=0
            while 6*a<=n:
                if (6*a+9*b+20*c)==n:
                    flag=1
                    ##print('possible comb. for ',n,' as-',a,', ',b,', ',c)
                    break
                a+=1
            b+=1
        c+=1
    if flag==0:
        count=0
        largestImpossibleComb=n
    else:
        count+=1
    n+=1
print('Largest number of McNuggets that cannot be bought in exact quantity:', largestImpossibleComb)
