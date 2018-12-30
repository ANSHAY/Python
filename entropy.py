import math
def entropy(probs):
    e=0
    for p in probs:
        e -= p * math.log(p) / math.log(2)
    print(e)
    
def input_probs():
    print("This app will calculate the entropy for the probabilities that you provide. :)  \n")
    print("enter the probabilities 1 by 1:")
    probs = []
    while True:
        i = input()
        probs = probs + [i]
        if (sum(probs)>=1):
            break
    print("Entropy for the entered probabilities is ---- \n")
    entropy(probs)
    print("Press enter to exit.....")
    input()
input_probs()
