# ps2d
x=int(input('enter the package sizes'))
y=int(input())
z=int(input())
packages = [x,y,z]
count=0
x=min(packages[0],packages[1],packages[2])
n=x
largestImpossibleComb=n-1
z=max(packages[0],packages[1],packages[2])
y=packages[0]+packages[1]+packages[2] - x - z
while count < x and n<=300:
    print('iteration for n= ',n)
    flag=0
    c=0
    while z*c<=n:
        b=0
        while y*b<=n:
            a=0
            while x*a<=n:
                if (x*a+y*b+z*c)==n:
                    flag=1
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
if(count<x):
    print('I don\'t want to spend more power on your silly question....   :|')
else:
    print('Given package sizes ',x,', ',y,',  and ',z,', the largest number of McNuggets that cannot be bought in exact quantity is:', largestImpossibleComb)
