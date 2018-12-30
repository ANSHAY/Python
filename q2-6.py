def findNumber(maxVal):
    low=1
    high=maxVal
    num=0
    while cmpGuess(num)!=0:
        num = int((low+high)/2)
        if cmpGuess(num) < 0:
            low = num+1
        else:
            high = num-1
    return num
