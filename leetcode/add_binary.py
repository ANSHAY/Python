# Given two binary strings a and b, return their sum as a binary string1.

# Here are some examples:

# Example 1: Input: a = "11", b = "1" Output: "100"

# Example 2: Input: a = "1010", b = "1011" Output: "10101"

# The constraints for the problem are:

# 1 <= a.length, b.length <= 10^4
# a and b consist only of ‘0’ or ‘1’ characters

def addBinary(a, b):
    l = len(a)-1
    r = len(b)-1
    c = 0
    res = ''
    
    while (l>=0 and r>=0):
        if a[l]=='0' and b[r]=='0':
            res += '1' if c else '0'
            c = 0
        elif a[l]=='1' and b[r]=='1':
            res += '1' if c else '0'
            c = 1
        else:
            res += '0' if c else '1'
            c = 1 if c else 0
        l -= 1
        r -= 1
    while (l>=0):
        res += '0' if ((a[l]=='1' and c==1) or (a[l]=='0' and c==0)) else '1'
        c = 1 if (a[l]=='1' and c==1) else 0
        l -= 1
    while (r>=0):
        res += '0' if ((b[r]=='1' and c==1) or (b[r]=='0' and c==0)) else '1'
        c = 1 if (b[r]=='1' and c==1) else 0
        r -= 1
    if c:
        res += '1'
    return res[::-1]    

print(addBinary('01100100', '0101001'))
print(addBinary('000000000', '111111111'))
print(addBinary('1111111111111', '111111111111'))
            
            