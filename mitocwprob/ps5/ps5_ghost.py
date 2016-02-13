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
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
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
word_list = load_words()

# TO DO: your code begins here!
def list_to_string(lst):

    return "".join(lst)

def is_valid_word(word, word_list):

    if (word in word_list)==False:
        return False

    return True

def is_valid_part(part, word_list):
    for i in word_list:
        part_length=len(part)
        word_length=len(i)
        if part_length<=word_length:
            if part == i[:part_length]:
                return True
    return False

def play_ghost():
    """
    function implementing ghost game
    """
    num_turn = 1
    who = 1
    turn = {1 : 'player 1', -1 : 'player2'}
    word = []

    while num_turn <= 3:
        # show word
        print list_to_string(word)

        # tell who's turn        
        print turn[who],"'s turn"

        # input letter
        letter=raw_input("input letter:")

        # append letter to the word         
        word.append(letter)

        # player lose when part of word is invalid        
        if is_valid_part(list_to_string(word), word_list)!=1:
            print turn[who],"has lost"
            return None

        num_turn += 1
        who = (-1)*who

    while num_turn > 3:
        # show word
        print list_to_string(word)

        # tell who's turn
        print turn[who],"'s turn"

        # input letter
        letter=raw_input("input letter:")

        # append letter to the word
        word.append(letter)

        # player lose when part of word is invalid
        if is_valid_part(list_to_string(word), word_list) != 1:
            print turn[who],"has lost"
            return None

        # player lose when word is valid
        if is_valid_word(list_to_string(word), word_list) == 1:
            print turn[who],"has lost"
            return None

        num_turn += 1
        who = (-1)*who



play_ghost()
