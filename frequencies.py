"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items: # for each item in the list
        if type(item) != str: #check if it is a string
            item = str(item) #if not, cast to a string
        if item in frequencies:
            frequencies[item] += 1 #if item is already in the dictionary, add to it's counter
        else:
            frequencies[item] = 1 #else add it to the dictionary
    return frequencies
