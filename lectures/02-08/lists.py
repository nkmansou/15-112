# declare a list

numbers = [3,5,6,9,10]
print numbers

words = ["hello","world"]
print words

# get the length (similar to strings)
print len(words)

# accessing elements (similar to strings)
print numbers[3]
print numbers[-1]
print numbers[1:4]

# loop through a list
# solution 1 (similar to strings)
for i in range(len(words)):
    print words[i]

# solution 2
for i in words:
    print i

# concatenating two lists (similar to strings)

others = ["how","are","you"]
print (words + others)

# check if an element is inside a list

print (9 in numbers)
print (91 in numbers)

def inside(n,l):
    for i in l:
        if i == l:
            return True
    return False

# remove an element from the list

words.remove("world")
print words

# add an element to the end of the list

words.append("you")
print words





