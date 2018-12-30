#ps3d
def subStringMatchExactlyOneSub(target,key):
    count=0
    t=()
    for i in range(0,len(target)-len(key)+1):
        count=0
        c=0
        for j in range(0,len(key)):
            if target[i+c]==key[j]:
                print('pass')
                count+=1
            c+=1
        if count==len(key)-1:
            t=t+(i,)
    print(t)
    ##return t
def test():
    subStringMatchExactlyOneSub('atgacatgcacaagtatgcat','a')
    input('enter')
    subStringMatchExactlyOneSub('atgacatgcacaagtatgcat','at')
    input()
    subStringMatchExactlyOneSub('atgacatgcacaagtatgcat','atg')
    input()
    subStringMatchExactlyOneSub('atgacatgcacaagtatgcat','atgc')
    input()
    subStringMatchExactlyOneSub('atgacatgcacaagtatgcat','atgca')
    input()
    subStringMatchExactlyOneSub('atgaatgcatggatgtaaatgcag','a')
    input()
    subStringMatchExactlyOneSub('atgaatgcatggatgtaaatgcag','at')
    input()
    subStringMatchExactlyOneSub('atgaatgcatggatgtaaatgcag','atg')
    input()
    subStringMatchExactlyOneSub('atgaatgcatggatgtaaatgcag','atgc')
    input()
    subStringMatchExactlyOneSub('atgaatgcatggatgtaaatgcag','atgca')
    input()
test()
