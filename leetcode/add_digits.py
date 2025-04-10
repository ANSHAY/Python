# /*
# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
# */
 
 # 34 --- 7
 # 653 -- 5
 # 5432 -- 5
 # 987654326789 -- 2
 # 1-9 -- 1-9
#  10-18 -- 1-9
#  19-27 -- 1-9

def add_digits(num):
    return 0 if num==0 else 9 if num%9==0 else num%9

print(add_digits(0))
print(add_digits(9))
print(add_digits(987654326789))
print(add_digits(5432))
print(add_digits(28))