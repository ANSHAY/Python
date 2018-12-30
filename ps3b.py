def subStringMatchExact(target,key):
    c=0
    count=0
    pos=[]
    for c in range(0,len(target)-len(key)):
        if key==target[c:c+len(key)]:
            count+=1
            pos.append(c)
        c+=1
    return pos
    
