def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]

def isPalindrome(s):
    if len(s)<=1:
        return True
    if first(s) == last(s):
        return isPalindrome(middle(s))
    else:
        return False

print (middle('aa'))
print(middle('ab'))
print(middle('a'))
print(middle(''))
print(isPalindrome('racecar'))
print(isPalindrome('huppa'))
    
