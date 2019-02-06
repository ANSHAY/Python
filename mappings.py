### This function generates the number of mappings
### that are posssible from an integer to a string
### such that every digit or a pair of digits can
### be mapped to a character from the alphabet
### input: an integer
### output: number of mappings

def mappings(num):
    m = 0
    if (num < 10):
        return 1
    if (num%10 >=1 and num%10<=26):
        m += mappings(num/10)
    if (num%100 >=10 and num%100<=26):
        m += mappings(num/100)
    return m
