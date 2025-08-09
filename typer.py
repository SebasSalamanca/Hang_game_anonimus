"""Plays a game where the user types random words within a time limit."""

import random
import time
import word_bank


def choose_user_level():
    user_level = ''
    while not (user_level == 'e' or user_level == 'm' or user_level == 'h'):
        user_level = input('Enter the level: easy = e, medium = m or hard = h: ').lower().strip()    
        print("\n")
    return user_level

def get_user_input(seconds):
    """Returns user_input if the user successfully completed the task."""
    user_input = ""
    # Run a stopwatch for the time it takes the user to respond.
    start = time.time()
    while not user_input.isalpha():
        user_input = input("(" + str(seconds) + " seconds) user input " + "\t").strip()
    stop = time.time()
    # Fail the round if a word is mispelled or if time runs out.
    within_time_limit = stop - start < seconds
    if within_time_limit: 
        return user_input
    else:
        print("\nYou exceed the time to write a letter -1 live.")
        return False

def pick_random_words(level):
    """Returns a random phrase containing the given number of words.""" 
    word = get_random_word(level)
    vector = ['_']*len(word)
    return word.strip(),vector

def compare_position_word(user_input, words_level, vector):
    flag = 0
    for i, j in enumerate(words_level):
        if user_input == j:
            flag = 1
            vector[i] = user_input  
    count = sum(1 for i in vector if i != '_')
    if count == len(words_level):
        flag = 7
    return vector, flag 

def show_user_screen(vector, lives):
    #Show the instructions the first time and then, lives and screen. 
    print(f"\n{''.join(vector)}\n")
    print(f'Lives remainig: {lives}\n')

def decrease_lives(number_lives, flag, word):
    if flag == 0:
        number_lives -= 1
    elif flag == 7:
        print('\nCongrats, you won!')
        return number_lives == 0 
    if number_lives == 0: 
        print("\nGame Over!")
        print(f'The word was: {word}')
    return number_lives
    

def get_random_word(mode):
    """Returns a random word with a word length based on the given mode."""
    if mode == "h":
        words = word_bank.hard_words
    elif mode == "m":
        words = word_bank.medium_words
    else:
        words = word_bank.easy_words

    return random.choice(words)