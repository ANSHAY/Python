for i in range(10,99):
    n = 11*i
    a=n/100
    c=n%10
    b=(n%100)/10
    x = a*a + b*b + c*c
    if x==i:
        print x
input()
