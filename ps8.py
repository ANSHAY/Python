# 6.00 Problem Set 8
#
# Intelligent Course Advisor
#
# Name:
# Collaborators:
# Time:
#

import time

MAXWORK = 190
SUBJECT_FILENAME = "subjects.txt"
VALUE, WORK = 0, 1

#
# Problem 1: Building A Subject Dictionary
#
def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """

    # The following sample code reads lines from the specified file and prints
    # each one.
    inputFile = open(filename)
    dic={}
    for line in inputFile:
        l=line.split(',')
        dic[l[0]] = (int(l[1]),int(l[2]))
    return dic

    # TODO: Instead of printing each line, modify the above to parse the name,
    # value, and work of each subject and create a dictionary mapping the name
    # to the (value, work).

def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = sorted(subjects.keys())
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print (res)
##printSubjects(loadSubjects(SUBJECT_FILENAME))

def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    return  val1 > val2

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return  work1 < work2

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return float(val1) / work1 > float(val2) / work2

#
# Problem 2: Subject Selection By Greedy Optimization
#
def greedyAdvisor(subjects, maxWork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """
    # TODO...
    localSubjects=subjects.copy()
    dic={}
    workPicked=0
    i=1
    while workPicked<=maxWork and len(localSubjects)>0:
        value=0
        work=1000
        for sub in localSubjects:
            if comparator(localSubjects[sub],(value,work)):
                value=localSubjects[sub][VALUE]
                work=localSubjects[sub][WORK]
                bestSubject=sub
        if workPicked+work<=maxWork:
            dic[bestSubject]=(value,work)
            workPicked += work
        del localSubjects[bestSubject]
    return dic
##subsV=greedyAdvisor(loadSubjects(SUBJECT_FILENAME), MAXWORK, cmpValue)
##subsW=greedyAdvisor(loadSubjects(SUBJECT_FILENAME), MAXWORK, cmpWork)
##subsR=greedyAdvisor(loadSubjects(SUBJECT_FILENAME), MAXWORK, cmpRatio)
##printSubjects(subsV)
##print('\n\nby work\n\n')
##printSubjects(subsW)
##print('\n\nby ratio\n\n')
##printSubjects(subsR)

def bruteForceAdvisor(subjectDict, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    nameList = list(subjectDict.keys())
    tupleList = list(subjectDict.values())
    bestSubset, bestSubsetValue = \
            bruteForceAdvisorHelper(tupleList, maxWork, 0, None, None, [], 0, 0)
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[nameList[i]] = tupleList[i]
    return outputSubjects

def bruteForceAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork):
    # Hit the end of the list.
    if i >= len(subjects):
        if bestSubset == None or subsetValue > bestSubsetValue:
            # Found a new best.
            return subset[:], subsetValue
        else:
            # Keep the current best.
            return bestSubset, bestSubsetValue
    else:
        s = subjects[i]
        # Try including subjects[i] in the current working subset.
        if subsetWork + s[WORK] <= maxWork:
            subset.append(i)
            bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue + s[VALUE], subsetWork + s[WORK])
            subset.pop()
        bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                maxWork, i+1, bestSubset, bestSubsetValue, subset,
                subsetValue, subsetWork)
        return bestSubset, bestSubsetValue

#
# Problem 3: Subject Selection By Brute Force
#
def bruteForceTime():
    """
    Runs tests on bruteForceAdvisor and measures the time required to compute
    an answer.
    """
    # TODO...
    subjectDict = loadSubjects(SUBJECT_FILENAME)
    respond='y'
    while respond=='Y' or respond =='y':
        maxWork = int(input("Enter the value of maxWork:    "))
        startTime = time.time()
        subsFinal=bruteForceAdvisor(subjectDict, maxWork)
        endTime = time.time()
        timeTaken = endTime-startTime
        print("time taken for maxWork = ",maxWork," is:   ",timeTaken)
        printSubjects(subsFinal)
        respond = input("Do you want to check more (y/n)?   ")
    print("byeeeeeeee!!!")
##bruteForceTime()

# Problem 3 Observations
# ======================
#
# TODO: write here your observations regarding bruteForceTime's performance

#
# Problem 4: Subject Selection By Dynamic Programming
#

def dpAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work) that contains a
    set of subjects that provides the maximum value without exceeding maxWork.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    # TODO...
    keys = list(subjects.keys())
    values = list(subjects.values())
##    without_i = {}
##    with_i = {}
    m={}
    w=[]
    i= len(keys)-1
    aW=maxWork
    for j in values:
            w.append(j[1])
    def DynamicPro(i,aW,m):
        try: return m[(i,aW)]
        except KeyError:
            if i==0:
                if w[i] <= aW:
                    dic={}
                    dic[keys[i]] = values[i]
                    m[(i,aW)] = dic.copy()
                    return dic.copy()
                else:
                    m[(i,aW)] = {}
                    return {}
            without_i={}
            without_i = DynamicPro(i-1, aW, m).copy()
            if w[i] > aW:
                m[(i, aW)] = without_i.copy()
                return without_i.copy()
            else:
                tempDic = DynamicPro(i-1, aW - w[i], m).copy()
                with_i={}
                for d in tempDic:
                    with_i[d] = tempDic[d]
                with_i[keys[i]] = values[i]
            sumWith_i=0
            for k in with_i.values():
                sumWith_i += k[0]
            sumWithout_i=0
            for k in without_i.values():
                sumWithout_i += k[0]
            if sumWith_i >= sumWithout_i:
                m[(i, aW)] = with_i.copy()
                return with_i.copy()
            else:
                m[(i, aW)] = without_i.copy()
                return without_i.copy()
    return DynamicPro(i,aW ,m)
##subjects = loadSubjects(SUBJECT_FILENAME)
##printSubjects(dpAdvisor(subjects, MAXWORK))
        
#
# Problem 5: Performance Comparison
#
def dpTime():
    """
    Runs tests on dpAdvisor and measures the time required to compute an
    answer.
    """
    # TODO...
    subjects = loadSubjects(SUBJECT_FILENAME)
    startTime=time.time()
    dic = dpAdvisor(subjects, MAXWORK)
    endTime=time.time()
    timeTaken = endTime-startTime
    print("time taken by dpAdvidor is:   ",timeTaken)
    printSubjects(dic)
dpTime()

# Problem 5 Observations
# ======================
#
# TODO: write here your observations regarding dpAdvisor's performance and
# how its performance compares to that of bruteForceAdvisor.
