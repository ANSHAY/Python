# computes and prints 100th prime number
import math
count = 1;
primeNumber = 3;
while count<1:
    for c in range(2,primeNumber):
        p=1
        if count%c==0:
            p=0
            break
    if p==1:
        count+=1
    primeNumber+=1
print count,'th prime number is',primeNumber
raw_input('enter')
