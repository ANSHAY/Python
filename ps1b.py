# computes and prints sum of log of all primes
import math
n = input("enter the limit of prime numbers till you want to compute the sum")
count = 3;
primeNumbers = 1;
sumLP = math.log(2)
while count <= int(n):
    for c in range(2,count):
        p=1
        if count%c==0:
            p=0
            break
    if p==1:
        primeNumbers+=1
        sumLP += math.log(count)
    count+=1
r=sumLP/int(n)
print('sum of log of prime number is',sumLP,'no. of prime numbers',primeNumbers)
print('ratio of two is',r)
