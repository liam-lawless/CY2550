#!/usr/bin/env python3

# CY2550 Project 4
# password generator
# Liam Lawless

import sys
import random as r

# open the file of words
file = open('words.txt')
  
# define a variable to read the lines of words.txt
line = file.readlines()

## define default values for pw output
words = 4
caps = 0
nums = 0
smbls = 0

listSymbols = ["~", "!", "@", "#", "$", "%", "^", "&", "*", ".", ":", ";"]

## defining it above for the sake of keeping match statement tidy
helpstr = """
usage: xkcdpwgen [-h] [-w WORDS] [-c CAPS] [-n NUMBERS] [-s SYMBOLS]
                
Generate a secure, memorable password using the XKCD method
                
optional arguments:
    -h, --help            show this help message and exit
    -w WORDS, --words WORDS
                          include WORDS words in the password (default=4)
    -c CAPS, --caps CAPS  capitalize the first letter of CAPS random words
                          (default=0)
    -n NUMBERS, --numbers NUMBERS
                          insert NUMBERS random numbers in the password
                          (default=0)
    -s SYMBOLS, --symbols SYMBOLS
                          insert SYMBOLS random symbols in the password
                          (default=0)"""

# define a function to randomly generate a password based on a set of user constraints
def pwgen(w, c, n, s):
    # result to append words to
    result = ""

    # list of 0's and 1's where 1 is an uppercase word and 0 is a lowercase word
    caps = [1] * c + [0] * (w - c)
    r.shuffle(caps)
    if n != 0:
        nums = [1] * n + [0] * (w - n)
        r.shuffle(nums)
    else:
        nums = [0] * w   
    if s != 0:    
        smbls = [1] * s + [0] * (w - s)
        r.shuffle(smbls)
    else:
        smbls = [0] * w

    # for the number of words w, pick a random word from words.txt
    for i in range(w):
        # generate a random number between 0 and the number of words in words.txt
        index = r.randint(0,len(line)-1)

        # string the "\n" off the end of str
        word = line[index].strip()
        
        # determine if str should be capitalized
        if caps[i] == 1:
            word = word.capitalize()
        
        # check if numbers is exhausted
        if nums[i] == 1:
            # pick a random number between 0 and 99
            num = r.randint(0,99)
            
            # 50/50 chance to append the number to the front or back of the word
            roll = r.randint(0,1)
            if roll == 1:
                word = str(num) + word
            elif roll == 0:
                word = word + str(num)
        
        # check if symbols is exhausted
        if smbls[i] == 1:
            # pick a random symbol from the list above
            symbol = listSymbols[r.randint(0, len(listSymbols) - 1)]

            # 50/50 chance to append the symbol to the fron or back of word
            roll = r.randint(0,1)
            if roll == 1:
                word = symbol + word
            elif roll == 0:
                word = word + symbol

        # append this word to either the front or back of result to randomize order of capitlization, etc.
        roll = r.randint(0,1)

        if roll == 1:
            result += word
        elif roll == 0:
            result = word + result    

    return result

#java style loop
if len(sys.argv) > 1:
    i = 1
    while i < len(sys.argv):
        # determing the argument(s) the user has input
        match sys.argv[i]:
            case "-h" | "--help":
                print(helpstr)
                break
            case "-w" | "--words":
                words = int(sys.argv[i+1])
                i+=1
            case "-c" | "--caps":
                caps = int(sys.argv[i+1])
                i+=1
            case "-n" | "--numbers":
                nums = int(sys.argv[i+1])
                i+=1
            case "-s" | "--symbols":
                smbls = int(sys.argv[i+1])
                i+=1
            case other:
                print("no match found: `" + sys.argv[i] +"'")
                break

        # increment i by one after every loop        
        i+=1

print(pwgen(words, caps, nums, smbls))