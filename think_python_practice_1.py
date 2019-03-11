import math


def total(initial=5, *numbers, **keywords):
    count = initial
    print (initial)
    print(numbers)
    print(keywords)
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]
    sec()
    return count

def sec():
    return True

def t(rr=4):
    print(rr)


def right_justify(s):
    l = len(s)
    print (' '*(70-l)+s)

def do_twice(f,v):
    f(v)
    f(v)

def print_twice(v):
    print (v)
    print (v)

def do_four(f, v):
    do_twice(f, v)
    do_twice(f, v)
   
def draw_grid(r=2, c=2):
    grid_line = ('+'+' - - - - ')*c+'+'
    grid_space = '|         '*c +'|'
    print (grid_line)
    for i in range(r):
        for j in range(4):
            print (grid_space)
        print (grid_line)

def do_n(f, n):
    if n<1:
        return
    for i in range(n):
        f()

def check_fermat(a, b, c, n):
    if n<=2:
        print ('n should be greater than 2')
        return
    lhs = a**n + b**n
    rhs = c**n
    if lhs == rhs:
        print ('Holy smokes, Fermat was wrong!')
    else:
        print ('No, that doesn’t work.')

def fermats_combo():
    print ('Checking fermat\'s theorem for a^n + b^n = c^n for n>2')
    a = int(input('Enter value of a:'))
    b = int(input('Enter value of b:'))
    c = int(input('Enter value of c:'))
    n = int(input('Enter value of n:'))
    check_fermat(a, b, c, n)

def is_triangle(a, b, c):
    d = [a, b, c]
    d.sort()
    if (d[0] + d[1]) > d[2]:
        print ('Yes')
    else:
        print ('No')

def check_triangle():
    a, b, c = map(int, input('Enter lengths of three edges of traingle:').strip().split())
    is_triangle(a, b, c)

def is_between(x, y, z):
    return y>= x and y<=z

def ack(m, n):
    if m==0:
        return n+1
    if m>0 and n==0:
        return ack(m-1, 1)
    if m>0 and n>0:
        return ack(m-1, ack(m, n-1))
    if m<0 or n<0:
        print ('arguments should be positive integers')

def is_power(a, b):
    if a==b:
        return True
    if a%b == 0:
        return is_power(a/b, b)
    else:
        return False

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def square_root(a):
    epsilon = 0.000001
    y = a/2
    while True:
        x = y
        y = (x + a/x)/2
        if abs(x-y)< epsilon:
            break
    return y

def eval_loop():
    result = 'no result yet'
    while True:
        inp = input('Enter a command (done to quit):')
        if inp == 'done':
            return result
        else:
            result = eval(inp)

def fact(x):
    if x<=1:
        return 1
    return x*fact(x-1)

def estimate_pi():
    k = 0
    summ = 0
    while True:
        term = (1103 + 26390*k)*fact(4*k)/(fact(k)**4 * 396**(4*k))
        if term < 1e-15:
            return 9801/(2*math.sqrt(2)*summ)
        summ += term
        k += 1

def is_palindrome(s):
    return s == s[::-1]

def rotate_word(word, n):
    res = ''
    for c in word:
        if c.isupper():
            res += chr((ord(c)+n-ord('A'))%26+ord('A'))
        else:
            res += chr((ord(c)+n-ord('a'))%26+ord('a'))
    return res

if __name__ == '__main__':
    #print(total(10, 1, 2, 3, vegetables=50, fruits=100))
    #t(5)
    #right_justify('tada')
    #do_twice(print_twice, 'spam')
    #draw_grid(5, 3)
    #do_n(draw_grid, 3)
    #check_fermat(3, 4, 5, 3)
    #fermats_combo()
    #is_triangle(8, 4, 6)
    #check_triangle()
    #print(is_between(2, 5, 8))
    #print(ack(3, 4))
    #print(is_power(25, 2))
    #print(gcd(48, 42))
    #print(square_root(49086543495))
    #print(eval_loop())
    #print(estimate_pi())
    #print(is_palindrome('ewefd'))
    #print(rotate_word('cheer', 7))

