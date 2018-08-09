''' Hangman game'''
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadwords():
    """
    Returns a list of valid words. Words are strings of lowercase letters
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    infile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = infile.readline()
    # wordlist: list of strings
    wordlist1 = line.split()
    print("  ", len(wordlist1), "words loaded.")
    return wordlist1

def chooseword(word_list1):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(word_list1)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadwords()

def iswordguessed(secret_word, lettersguessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    count = 0
    for index in secret_word:
        if index in lettersguessed:
            count += 1
        else:
            count = 0
    if count == len(secret_word):
        return True
    return False
def getguessedword(secret_word, letters_guessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    list1 = ''
    for index in secret_word:
        if index in letters_guessed:
            list1 += index
        else:
            list1 += ("-")
    return list1


def getavailableletters(letters_guessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    remaining = []
    letters = string.ascii_lowercase
    remaining = [index for index in letters if index not in letters_guessed]
    return ''.join(remaining)
def hangman(secretword1):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.
    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    secretword1 = chooseword(wordlist).lower()
    letters_guessed = []
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secretword), "letters long")
    flag = False
    maxguessletters = len(secretword1)+5
    remove_letters = []
    while maxguessletters != 0:
        print("-----------")
        print("You have ", maxguessletters, "guesses left")
        print("Available Letters ", getavailableletters(letters_guessed))
        guess = input("Please guess a letter: ")
        maxguessletters -= 1
        letters_guessed.append(guess)
        if guess in getavailableletters(remove_letters):
            print(getguessedword(secretword1, letters_guessed))
        else:
            print("Oops! No repetition: ", getguessedword(secretword1, letters_guessed))
        if guess not in secretword1:
            print("Oops! Not in my word: ", getguessedword(secretword1, letters_guessed))
        if iswordguessed(secretword1, letters_guessed) is True:
            flag = True
            break
        else:
            flag = False
        remove_letters += guess
    if flag is True:
        print("Good guess: ", getguessedword(secretword1, letters_guessed))
        print("------------")
        print("Congratulations, You Won!")
    else:
        print("Sorry you ran out of guesses. The word was ", secretword1)
    guess = input()



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretword = chooseword(wordlist).lower()
hangman(secretword)
