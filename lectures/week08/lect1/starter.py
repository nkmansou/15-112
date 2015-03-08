import string
import os

# the function "clean" takes a string and removes the punctuation, normalize whitespaces, removes tabulations and linebreaks and converts all letters to lowercase.
def clean(s):
    import sets
    import string
    # # remove punctuation symboles
    # for c in string.punctuation:
    #     s= s.replace(c,"")
    # normalize whitespaces
    for c in string.whitespace:
        s= s.replace(c," ")
    # convert to lowercase
    s = s.lower()
    # keep letters and space only
    letters = sets.Set(string.ascii_lowercase)
    s = ''.join( [ i for i in s if i in letters or i == " "])
    return s

# problem 1: write a function "count" that takes a filename and returns the number of words contained in this file

# problem 2: write a function "getWords" that takes a filename and returns a sorted list of all words contained in this file without duplicate

# problem 3: write a function "analyze" that takes a filename and produces another file called "filename_result.txt" (where "filename" is the name of the original file) that contains the list of all words contained in the input file. Each word should be on a seperate line.


