import os

# the function clean takes a string and removes the punctuation, normalize whitespaces, removes tabulations and linebreaks and converts all letters to lowercase.
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


# read the file input_file.txt
file = open(os.path.dirname(os.path.realpath(__file__)) + "/input_file.txt")
lines = file.readlines()

# print each line
for line in lines:
    print line


# clean each line and print it
for line in lines:
    print clean(line)


# write each line in a new file
# print the result
result = open(os.path.dirname(os.path.realpath(__file__)) + "/output_file.txt","w")
# for each line
for line in lines:
    l = clean(line)
    result.write(l)
result.close()