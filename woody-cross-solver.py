#!/usr/bin/env python3
#################################################
''' "Woody Cross" Solver

This script is meant to solve puzzles in the "Woody Cross" app.
It prompts for a set of letters to work with, returns a list of words
which can be made from these letters.

Note: this takes all of the fun and challenge out of Woody Cross.

*** Usage: Expects to find "wordlist.txt" in the pwd
       Most online dictionaries were too long (and included uselss words like "FFFFF").
       I ended-up downloading an English "spelling word" list, dropping any words which
       were shorter than four characters.

'''

globalPerms=[]

def permutations(string):
    """
    Create all permutations of a string with non-repeating characters
    """
    permutation_list = []
    if len(string) == 1:
        return [string]
    else:
        for char in string:
            [permutation_list.append(char + a) for a in permutations(string.replace(char, "", 1))]
    for x in permutation_list:
        globalPerms.append(x)
    return permutation_list


##################################################
# Read dict file into list
dict = open("wordlist.txt", "r")
dictList=[]
for dictWord in dict:
    dictList.append(dictWord.rstrip())
dict.close()

print("enter letters to work with: ", end='')
wordlist = input()

permList=permutations(wordlist)

answer=[]
for word in globalPerms:
    if word in dictList:
        if word not in answer:
            answer.append(word)

for i in answer:
    print(i)
