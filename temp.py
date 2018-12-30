##try:
##    h={'a':1,'s':2,'d':3}
##    print(h['a'])
##    if h['a'] == 1:
##        print("running")
##except:
##    print("except rUns")
    
##def test(var):
##    print('local var with value from global var',var)
##    var=50
##    print('local var with new value',var)
##var=70
##print('global var  ',var)
##test(var)
##print('global var after calling test',var)

def test(dic):
    print('local dic with value from global dic',dic)
    dic['i']=50
    print('local dic with new value',dic)
dic={'a':70,'i':80,'k':60}
print('global dic  ',dic)
test(dic)
print('global dic after calling test',dic)

