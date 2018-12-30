# Problem Set 4
# Name: 
# Collaborators: 
# Time: 

#
# Problem 1
#

def nestEggFixed(salary, save, growthRate, years):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: the annual percent increase in your investment account (an
      integer between 0 and 100).
    - years: the number of years to work.
    - return: a list whose values are the size of your retirement account at
      the end of each year.
    """
    # TODO: Your code here.
    F = []
    if years==1:
        F.append(float(salary)*float(save)*0.01)
        return F
    else:
        F = nestEggFixed(salary, save, growthRate, years-1)
        F.append(F[-1]*(1.0+0.01*float(growthRate))+salary*save*0.01)
        return F

def testNestEggFixed():
    salary     = 10000
    save       = 10
    growthRate = 15
    years      = 5
    savingsRecord = nestEggFixed(salary, save, growthRate, years)
    print (savingsRecord)
    # Output should have values close to:
    # [1000.0, 2150.0, 3472.5, 4993.375, 6742.3812499999995]

    # TODO: Add more test cases here.
    salary     = 100000
    save       = 15
    growthRate = 15
    years      = 3
    savingsRecord = nestEggFixed(salary, save, growthRate, years)
    print (savingsRecord)
    
    salary     = 60000
    save       = 15
    growthRate = 12
    years      = 1
    savingsRecord = nestEggFixed(salary, save, growthRate, years)
    print (savingsRecord)

#
# Problem 2
#

def nestEggVariable(salary, save, growthRates):
    # TODO: Your code here.
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: a list of the annual percent increases in your investment
      account (integers between 0 and 100).
    - return: a list of your retirement account value at the end of each year.
    """
    F = []
    y = len(growthRates)
    if y==1:
        F.append(float(salary)*float(save)*0.01)
        return F
    else:
        F = nestEggVariable(salary, save, growthRates[0:y-1])
        F.append(F[-1]*(1.0+0.01*float(growthRates[-1]))+salary*save*0.01)
        return F
    

def testNestEggVariable():
    salary      = 10000
    save        = 10
    growthRates = [3, 4, 5, 0, 3]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print (savingsRecord)
    # Output should have values close to:
    # [1000.0, 2040.0, 3142.0, 4142.0, 5266.2600000000002]

    # TODO: Add more test cases here.
    salary     = 100000
    save       = 15
    growthRates = [1, 5, 8, 2]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print (savingsRecord)
    
    salary     = 60000
    save       = 15
    growthRates = [0, 1, 12]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print (savingsRecord)
    

#
# Problem 3
#

def postRetirement(savings, growthRates, expenses):
    """
    - savings: the initial amount of money in your savings account.
    - growthRate: a list of the annual percent increases in your investment
      account (an integer between 0 and 100).
    - expenses: the amount of money you plan to spend each year during
      retirement.
    - return: a list of your retirement account value at the end of each year.
    """
    # TODO: Your code here.
    F = []
    y = len(growthRates)
    if y==1:
        F.append(float(savings)*(1+0.01*growthRates[0])-expenses)
        return F
    else:
        F = postRetirement(savings, growthRates[0:y-1],expenses)
        F.append(F[-1]*(1.0+0.01*float(growthRates[-1]))-expenses)
        return F

def testPostRetirement():
    savings     = 100000
    growthRates = [10, 5, 0, 5, 1]
    expenses    = 30000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print (savingsRecord)
    # Output should have values close to:
    # [80000.000000000015, 54000.000000000015, 24000.000000000015,
    # -4799.9999999999854, -34847.999999999985]

    # TODO: Add more test cases here.
    savings     = 1000000
    growthRates = [7, 3, 0, 2, 5, 8, 7, 1]
    expenses    = 99000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print (savingsRecord)

    savings     = 40000
    growthRates = [9, 12, 15, 1, 9, 4, 13, 9, 6]
    expenses    = 6000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print (savingsRecord)

#
# Problem 4
#

def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates,
                    epsilon):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - preRetireGrowthRates: a list of annual growth percentages on investments
      while you are still working.
    - postRetireGrowthRates: a list of annual growth percentages on investments
      while you are retired.
    - epsilon: an upper bound on the absolute value of the amount remaining in
      the investment fund at the end of retirement.
    """
    # TODO: Your code here.
    savingsList = nestEggVariable(salary, save, preRetireGrowthRates)
    savings = savingsList[-1]
    fundInEnd=1000
    low=0
    high=savings
    while not((fundInEnd > 0-epsilon) and (fundInEnd < 0)):
        expenses = (low+high)/2
        F = postRetirement(savings, postRetireGrowthRates, expenses)
        fundInEnd = F[-1]
        if fundInEnd > epsilon:
            low=expenses
        if fundInEnd < 0-epsilon:
            high=expenses
        ##print(expenses)
    return expenses

def testFindMaxExpenses():
    salary                = 10000
    save                  = 10
    preRetireGrowthRates  = [3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1]
    epsilon               = .01
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates, epsilon)
    print (expenses)
    # Output should have a value close to:
    # 1229.95548986

    # TODO: Add more test cases here.
    salary                = 10000
    save                  = 10
    preRetireGrowthRates  = [3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1]
    epsilon               = .01
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates, epsilon)
    print (expenses)

    salary                = 60000
    save                  = 10
    preRetireGrowthRates  = [2, 4, 5, 1]
    postRetireGrowthRates = [1, 5, 0, 5, 1]
    epsilon               = .01
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates, epsilon)
    print (expenses)
