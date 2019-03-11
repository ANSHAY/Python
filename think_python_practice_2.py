def print_words(condition, letters, prnt=True):
    f = open('words.txt')
    w = f.readline().strip().lower()
    count = 0
    total_words = 0
    while w:
        total_words += 1
        if condition(w, letters):
            count += 1
            if prnt:
                print (w)
        w = f.readline().strip().lower()
    f.close()
    return count, total_words

def avoids(word, letters):
    for l in letters:
        if l in word:
            return False
    return True

def no_of_words_without_forbidden_letters():
    letters = input('Enter a string of forbidden letters: ').strip()
    count, total = print_words(avoids, letters, False)
    print ('Number of words without forbidden letters: ', count)
    
def uses_only(word, letters):
    for w in word:
        if w not in letters:
            return False
    return True

def uses_all(word, letters):
    for l in letters:
        if l not in word:
            return False
    return True

def has_no_e():
    count, total_words = print_words(avoids, 'eE', prnt=True)
    print ('Words that have no e:', count, 'of', total_words)
    print ('Percent of words that have no e:', (count*100/total_words), '%')

def is_abecedarian(word, dummy=''):
    w = word[0]
    for i in range(1, len(word)):
        if w > word[i]:
            return False
        w = word[i]
    return True

def is_triple_pair(word, dummy=''):
    i = 0
    count = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            count += 1
            if count == 3:
                return True
            i += 2
        else:
            i += 1
            count = 0
    return False

def is_palindrome(s):
    return s == s[::-1]

def odometer_pal():
    for i in range(100000, 1000000):
        s = str(i)
        if is_palindrome(str(i)[2:]):
            if is_palindrome(str(i+1)[1:]):
                if is_palindrome(str(i+2)[1:-1]):
                    if is_palindrome(str(i+3)):
                        print (i)

def find_age():
    for a in range(0, 100):
        m = (a%10)*10 + a//10
        pal_times = []
        if m<a+10:
            continue
        i = a
        while m<100:
            if str(i).zfill(2) == str(m)[::-1].zfill(2):
                pal_times.append(i)
            i += 1
            m += 1
        if len(pal_times)==8:
            print ('possible current age:', pal_times[5])

def middle(lst):
    return lst[1:-1]

def chop(lst):
    lst.pop(0)
    lst.pop(-1)
    return None

def is_sorted(lst):
    prev = lst[0]
    for l in lst:
        if l<prev:
            return False
        prev = l
    return True

def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    l1 = list(str1).sort()
    l2 = list(str2).sort()
    return l1==l2

def bisect(lst, val):
    i = 0
    l = len(lst)
    m = (i+l)//2
    if not lst:
        return None
    if lst[m] == val:
        return m
    elif lst[m] < val:
        i = m+1
        return bisect(lst[i:l], val)
    else:
        l = m
        return bisect(lst[i:l], val)

def interlock(word_list):
    for word in word_list:
        word1 = word[0::2]
        word2 = word[1::2]
        if bisect(word_list, word1) and bisect(word_list, word2):
            print (word1, word2)
            return True
        return False

def has_duplicates(lst):
    d = dict()
    for l in lst:
        if d.get(l, 0):
            return True
        else:
            d[l] = 1
    return False

def remove_duplicates(lst):
    return list(set(lst))
            
if __name__ == '__main__':
    #has_no_e()
    #print(avoids('abrakadabra', 'efgth'))
    #no_of_words_without_forbidden_letters()
    #print(uses_only('assasaaassssasasassaassa', 'as'))
    #print(uses_all('akcbhuja', 'aeiou'))
    #print(print_words(uses_all, 'aeiouy', False))
    #print(is_abecedarian('abcddeefghiajklprtz'))
    #print(print_words(is_abecedarian, '', False))
    #print(print_words(is_triple_pair, '', True))
    #odometer_pal()
    #find_age()
    #print(middle([1,2,3,4,5]))
    #l = [1,2,3,4,5,6]
    #chop(l)
    #print (l)
    #print(is_sorted([1,2,3,4,5,3,5,6,6,7,8,99])
    #print(is_anagram('asdfghjl','lkjgfdssa'))
    #print(bisect([1,2,3,4,5,6,7,8,9], 10))
    #print(has_duplicates([1,2,3,4,5,6,5,4,3,2]))
    #print(remove_duplicates([1,2,3,4,5,4,3,2,1,6,7,6,8]))
