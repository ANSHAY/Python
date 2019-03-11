def invert_dict(d):
    inv = {}
    for k in d:
        inv.setdefault(d[k], []).append(k)
    return inv

known = {}
def ack(m,n):
    if (m,n) in known:
        return known[(m,n)]
    if m==0:
        known[(m,n)] = n+1
        return n+1
    if n==0:
        known[(m,n)] = ack(m-1, 1)
        return known[(m,n)]
    if m>0 and n>0:
        known[(m,n)] = ack(m-1, ack(m, n-1))
        return known[(m,n)]

def make_word_dict():
    d = {}
    f = open('words.txt')
    for w in f:
        d[w.strip().lower()] = 1
    f.close()
    return d

def rotate_word(word, i):
    res = ''
    for w in word:
        res += chr((ord(w)-97+i)%26+97)
    return res

def all_rotate_pairs(word_dict):
    i = 0
    d = {}
    for word in word_dict:
        for i in range(1, 14):
            rotated = rotate_word(word, i)
            if rotated in word_dict:
                d.setdefault(word, []).append(rotated)
                print (word, i, rotated)
    return (d)

from pronounce import read_dictionary
def homophones():
    dic = read_dictionary('c06d.txt')
    for word in dic:
        word1 = word[1:]
        word2 = word[0]+word[2:]
        if word1 not in dic:
            continue
        if word2 not in dic:
            continue
        if dic[word1] == dic[word] and dic[word2] == dic[word]:
            print (word)
    return

if __name__ == '__main__':
    #print(invert_dict({1:2, 3:4, 5:6, 7:4}))
    #print(ack(3,6))
    #print(rotate_word('asdfg', 12))
    #d = make_word_dict()
    #print(all_rotate_pairs(d))
    homophones()

