# Problem Set 5: Ghost
# Name: 
# Collaborators: 
# Time: 
#

import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', -1)
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

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()

# TO DO: your code begins here!
def is_valid_letter(letter):
    return letter in string.ascii_letters

def update_word(word,letter):
    letter = letter.lower()
    return word+letter
def ghost():
    print("Welcome to GHOST >>>...")
    print("player 1 warm up!! You have to go first.... ")
    word=''
    ##flag=0
    letter=input("current word fragment: ''\nEnter a letter:  ")
    count=1
    while is_valid_letter(letter):
        word = update_word(word,letter)
        flag=0
        for s in wordlist:
            if word==s and count>3:
                print(word," is a word")
                print("player ",(count+1)%2+1,"looses")
                return
            if word == s[0:len(word)]:
                flag=1
        if flag==0:
            print("\nno word starts with ",word)
            print("player ",(count+1)%2+1,"looses")
            return
        count+=1
        print()
        print("Current word fragment: ",word)
        print("player ",(count+1)%2+1,"'s turn")
        letter=input("Enter a letter:  ")
    print("invalid letter!!!   player ",(count+1)%2+1,"looses")
ghost()


    
