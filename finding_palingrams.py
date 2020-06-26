#!/usr/bin/env python3
import sys 
from load_dictionary import load

file = "dictionary.txt"

wordList = load(file)
list_of_palindromes = []

for word in wordList:
    if ( (len(word) > 1) and (word == word[::-1]) ):
        list_of_palindromes.append(word)

# print("list of palindromes: ", list_of_palindromes)
print("\nNumber of palindromes found = {}\n".format(len(list_of_palindromes)))
print(*list_of_palindromes, sep=', ')
