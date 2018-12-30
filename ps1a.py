# computes and prints 100th prime number
import math
count = 3;
primeNumbers = 1;
while primeNumbers<1000:
    for c in range(2,count):
        p=1
        if count%c==0:
            p=0
            break
    if p==1:
        primeNumbers+=1
    count+=1
print('1000th prime number is',count)
