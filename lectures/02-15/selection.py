# find the minimum value of a list given as argument
def min(l):
    # initialize the current minimum
    m = l[0]
    # for each element of l
    for n in l:
        # if this element is smaller than my current minimum
        if n<m:
            # store this element in my current minimum
            m = n
        # else nothing
    # return the minimum
    return m

# sort a list given as argument
def selectionSort(l):
    # create an empty result list
    res = []
    # while l is not empty
    while not(l==[]):
        # find the minimum of l
        m = min(l)
        # remove it from l
        l.remove(m)
        # add it to the result l
        res.append(m)
    # return the list result
    return res

myList = [81, 2, 32, 91, 15, 31, 42]
test = selectionSort(myList)
print test

