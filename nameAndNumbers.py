## 1.a  python version 3.2.2

def nameAndNumber():
    array1 = ['ANSHAY','name2','name3','name4','many','more','names','in','this','way']
    array2 = ['1','2','3','4','5','6','7','8','9','10']
    response='y'
    while response=='y'or response=='Y':
        flag=0
        name=input('Enter a name:    ')
        for i in range(0,len(array1)):
            if name==array1[i]:
                print('corresponding number in array2 is',array2[i])
                flag = 1
                break
        if(flag==0):
            num = int(input('The name is not in the array, enter the corresponding number of the name to add it to the array:  '))
            array1.append(name)
            array2.append(num)
            print('name: ',name,' and number: ',num,' are added to the arrays.')
        response = input('Do you want to check more (y/n):')
    print('have a nice day!!')
nameAndNumber()
    
