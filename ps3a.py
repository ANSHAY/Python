#ps3a: count substring matches using iteration and recursion

import string

def countSubStringMatch (target,key):
    match=0
    c=0
    while c<= len(target)- len(key):
        p=c
        for k in range(0,len(key)):
            if target[p]==key[k]:
                p+=1
                print('pass')
            else:
                print('gas!!')
                break
        if p==(c+len(key)):
            match+=1
            #c=p
            c+=1
        else:
            c+=1
    return match

def countSubStringMatchRecursive (target,key):
    ##if len(target)>=len(key):
    ##    match=countSubStringMatchRecursive(target[1:len(target)],key)
    ##else:
    ##    return 0
    ##if (target[0:len(target)]==key):
    ##    return match+1
    ##else:
    ##    return match
    if len(target)<len(key):
        return 0
    m1=0
    if key==target[0:len(key)]:
        m1=1
    m2=countSubStringMatchRecursive(target[1:len(target)],key)
    return m1+m2
    
