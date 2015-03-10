import string
import os
import re

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
    return re.sub(r'[^\x00-\x7F]',' ', s)

# problem 1: write a function "count" that takes a filename and returns the number of words contained in this file

def count(filename):
    # read the file
    file = open(os.path.dirname(os.path.realpath(__file__)) + "/" + filename)
    # read all the lines: lines is a list of strings
    lines = file.readlines()
    # start counter at 0
    c = 0
    # for each line
    for line in lines:
        # clean the line and I split
        cleanLine = clean(line)
        # split the line (string) into a list of words
        l = cleanLine.split(" ")
        # loop through all words
        for i in l:
            if i != "":
                c = c + 1;
    return c

# print count("SherlockHolmes.txt")

# problem 2: write a function "getWords" that takes a filename and returns a sorted list of all words contained in this file without duplicate

def getWords(filename):
    res = []
    file = open(os.path.dirname(os.path.realpath(__file__)) + "/" + filename)
    lines = file.readlines()
    for line in lines:
        cl = clean(line)
        l = cl.split(" ")
        for word in l:
            if word !="":
                if not(word in res):
                    res.append(word)
    res.sort()
    return res

# print getWords("SherlockHolmes.txt")

# problem 3: write a function "analyze" that takes a filename and produces another file called "filename_result.txt" (where "filename" is the name of the original file) that contains the list of all words contained in the input file. Each word should be on a seperate line.

def analyze(filename):
    l = getWords(filename)
    res_filename = filename.split(".")[0] + "_result.txt"
    out = open(os.path.dirname(os.path.realpath(__file__)) + "/" + res_filename,"w")
    for i in l:
        out.write(i + "\n")
    out.close()

analyze("SherlockHolmes.txt")




