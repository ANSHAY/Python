import math
def entropy(probs):
    L=0
    for p in probs:
        L += p[0] * p[1]
    print(L)
    input()
def input_probs():
    print("!!!!enter 0 when you want to compute!!!!")
    print("enter the probabilities and length 1 by 1:")
    probs = []
    while True:
        i = input()
        if (i==0):
            break
        l = input()
        probs += [[i,l]]
    entropy(probs)
input_probs()
