# Problem Set 5: 6.00 Word Game
# Name: 
# Collaborators: 
# Time: 
#

import random
import string
import time

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
points_dic = {}
rearrange_dict={}

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def get_words_to_points(word_list):
    """ Return a dict that maps every word in word_list to its point value."""
    for s in word_list:
        points_dic[s]=get_word_score(s,100)
    return points_dic

def get_word_rearrangements(word_list):
    d={}
    for w in word_list:
        string=''
        length=0
        stringList = sorted(w)
        for i in range(len(stringList)):
            string = string + stringList[i]
        d[string]=w
    return d
    

##def pick_best_word(hand, points_dict):
##    """ Return the highest scoring word from points_dict that can be made with thegiven hand.
##    Return '.' if no words can be made with the given hand."""
##    ##...implement me!...
##    bestScore = 0
##    bestWord = '.'
##    dicOfLetters={}
##    for s in points_dic.keys():
##        for k in hand:
##            dicOfLetters[k]=hand[k]
##        flag=1
##        for i in s:
##            if flag==0:
##                break
##            if i in hand and dicOfLetters.get(i,0)>0:
##                dicOfLetters[i] = dicOfLetters.get(i,0)- 1
##            else:
##                flag=0
##        if flag==1:
##            if points_dic[s] > bestScore:
##                bestScore = points_dic[s]
##                bestWord = s
##    return bestWord


##def pick_best_word_faster(hand, points_dict):
##    ## to find a subset of hand and store it to 'subset'
##    c=len(hand)
##    while c>1:
##        subset=findSubset(hand)
##        bestWord='.'
##        bestScore=0
##        w=' '
##        length=0
##        for l in subset:
##            for s in w:
##                if s<l:
##                    length+=1
##                else:
##                    break
##            w=w[0:length]+l+w[length:len(w)-1]
##
##        if w in rearrange_dict:
##            if points_dict[rearrange_dict[w]]>bestScore:
##                bestScore=points_dict[rearrange_dict[w]]
##                bestWord=rearrange_dict[w]
##        c-=1
##    return bestWord

def findSubsets(s):
    """ Returns list containing subsets of argument """
    if len(s) == 1:
        return s
    else:
        ssc = findSubsets(s[1:])
        return [s[0]] + [s[0]+str(comb) for comb in ssc] + ssc

def pick_best_word_faster(hand,rearrange_dict):
    keys = list(hand.keys())
    handString = ''
    bestScore = 0
    bestWord = '.'
    for k in hand.keys():
        handString += k*hand[k]
            
    sortedHandString = sorted(handString)
    subsets = findSubsets(sortedHandString)
    for s in subsets:
        if s in rearrange_dict.keys():
            score = points[rearrange_dict[s]]
            if score > bestScore:
                bestWord = rearrange_dict[s]
                bestScore = score
    return bestWord
    

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    inFile = open("words.txt",'r',-1)
    ##(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print ("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    The score for a word is the sum of the points for letters
    in the word, plus 50 points if all n letters are used on
    the first go.

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    # TO DO ...
    score=0
    for i in word:
        score += SCRABBLE_LETTER_VALUES[i]
    if n==len(word):
        return score+50
    return score

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """

    for letter in hand.keys():
        for j in range(hand[letter]):
            print (letter,end=' ')             # print all on the same line
    print ()                                   # print an empty line

#
# Make sure you understand how this function works and what it does!
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = int(n / 3)
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not mutate hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ...

    for i in word:
        hand[i] = hand.get(i,0) - 1
        ##print(i,' ',hand.get(i,0))
    return hand

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    # TO DO ...
    memo={}
    for i in word:
        if not (i in hand):
            return False
        if i in memo:
            memo[i] = memo.get(i,0)-1
            if memo[i]==-1:
                return False
        else:
            memo[i]=hand.get(i,0)-1
        
    try:
        if points_dic[word]>0:
            return True
    except:
        return False
            

#
# Problem #4: Playing a hand
#
def play_hand(hand, word_list):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word and the total
      score so far are displayed, the remaining letters in the hand 
      are displayed, and the user is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

    * The final score is displayed.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
    """
    # TO DO ...
    finalScore = 0
    timeLimit = float(input("enter time limit:  "))
    print('Your hand is--->',end='     ')
    display_hand(hand)

    ##word = input("enter word from the hand or . to terminate....")
    start_time = time.time()
    word = pick_best_word_faster(hand, rearrange_dict)
    end_time = time.time()
    totalTimeTaken= end_time-start_time
    remainingTime = timeLimit - float(totalTimeTaken)
    print("The word is:   ",word,"\nIt took ",totalTimeTaken," secs to answer")
    while word != '.':
        if remainingTime<0:
            print("Time Limit exceeded")
            break
        print("\tYou have ",remainingTime," seconds remaining")
        if not is_valid_word(word, hand, word_list):
            print("\twrong input. Try again....")
        else:
            score = get_word_score(word, HAND_SIZE) / (totalTimeTaken+2)
            finalScore += score
            print('\n\t',word,'  made  ',score,'  points.\nYour total score is:  ',finalScore)
            hand = update_hand(hand,word)
            print('\n\tcurrent hand is:  \t',end=' ')
            display_hand(hand)
        start_time = time.time()
        word = pick_best_word_faster(hand, rearrange_dict)
        end_time = time.time()
        totalTimeTaken= end_time-start_time
        remainingTime = remainingTime - float(totalTimeTaken)
        print("\tIt took ",totalTimeTaken," secs to answer")
        
        
    print("\nYour final score is:  ", finalScore)
    

#
# Problem #5: Playing a game
# Make sure you understand how this code works!
# 
def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """
    # TO DO ...
    ##print ("play_game not implemented.")         # delete this once you've completed Problem #4
    ##play_hand(deal_hand(HAND_SIZE), word_list) # delete this once you've completed Problem #4
    
    ## uncomment the following block of code once you've completed Problem #4
    hand = deal_hand(HAND_SIZE) # random init
    while True:
        cmd = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if cmd == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand(hand.copy(), word_list)
            print ()
        elif cmd == 'r':
            play_hand(hand.copy(), word_list)
            print ()
        elif cmd == 'e':
            break
        else:
            print ("Invalid command.")

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    global points
    points = get_words_to_points(word_list)
    rearrange_dict = get_word_rearrangements(word_list)
    play_game(word_list)
