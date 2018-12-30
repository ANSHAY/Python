
FILE_NAME1 = "data after count algo.txt"
FILE_NAME2 = "input for 2nd round.txt"

def readFile():
    data = open(FILE_NAME1)
    data = data.read()
    newData = open(FILE_NAME2)
    newData.write('q')
    for i in data:
        if i == '1':
            newData.write("1111")
            print('was here')
        elif i == '2':
            newData.write('0000')
        elif i == '3':
            newData.write('1110')
        elif i == '4':
            newData.write('0001')
        elif i == '5':
            newData.write('110')
        elif i == '6':
            newData.write('001')
        elif i == '7':
            newData.write('10')
        elif i == '8':
            newData.write('01')
    print(newData.read())
readFile()
