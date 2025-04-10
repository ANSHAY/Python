# Given two strings s and t, return true if they are equal when both are typed into empty text editors. ‘#’ means a backspace character

def backComp(s, t):
    return back(s) == back(t)

def back(s):
    stack = []
    for c in s:
        if c!='#':
            stack.append(c)
        elif len(stack)>0:
            stack.pop()
    return stack

