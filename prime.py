import math

MAX_LIMIT = 5000
global prime
prime = {0:2}
count = 3
def primeNumbers():
    global count
    c = 0
    for p in range(1,MAX_LIMIT):
        c += 1
        if isPrime(p):
            prime[count] = p
            count += 1
            if c%4 == 0:
                print(p)
            else:
                print(str(p)+'\t')
        #else:
            #if c%4 == 0:
                #print('*')
            #else:
                #print('*\t')
            
    ##print(prime)

def isPrime(p):
    if p == 1 : return False
    s = int(math.sqrt(p))
    for i in prime.values():
        if i > s:
            break
        if p % i == 0:
            return False
    return True

def printPrime():
    c=1
    for i in prime.values():
        print(i,'\t')
        if c % 4 ==0:
            print('\n')
        c += 1
        
primeNumbers()        
##printPrime()        
