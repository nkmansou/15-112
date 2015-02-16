# insert a number in a sorted list
def insert(n,l):
    # the goal is to find the right index in the list
    # where to insert the value n
    # create an index value
    i = 0
    # while the current element at i is smaller than n
    # or the end of the list has been reached
    while(i<len(l) and l[i] < n):
        # go to the next one
        i = i + 1
    # create the new list
    l = l[:i] + [n] + l [i:]
    return l

# sort a list given as argument
def insertionSort(l):
    # create an empty result list
    res = []
    # for each element in l
    for n in l:
        # insert it in the list result
        res = insert(n,res)
    # return the list result
    return res

myList = [81, 2, 32, 91, 15, 31, 42]
test = insertionSort(myList)
print test

