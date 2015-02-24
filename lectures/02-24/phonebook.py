def getNumber(book,name):
    if name in book:
        return book[name]
    else:
        return "Not in your phone book!"

def getName(book,number):
    for k in book:
        if book[k] == number:
            return  k
    return "Not in your phone book!"

def insert(book, name, number ):
    if name in book:
        return False
    else:
        book[name] = number
        return True

def update(book, name, number ):
    if name in book:
         book[name] = number
         return True
    else:
        return False

def addQatarPrefix(book, key):
    if not(book[key][0:4] == "+974"):
        book[key] = "+974 " + book[key]

def addQatarPrefixToAll(book):
    for k in book:
        addQatarPrefix(book,k)

#### tests ####

test = {"PersonA": "1111 2222", "PersonB": "3333 4444", "PersonC": "5555 6666"}

print getNumber(test,"PersonA")
print getNumber(test,"PersonD")

print getName(test,"3333 4444")
print getName(test,"77777 8888")

print test
print insert(test,"PersonD", "+974 77777 8888")
print test
print insert(test,"PersonB", "+974 99999 9999")

print test
print update(test,"PersonB", "+974 99999 9999")
print test
print update(test,"PersonE", "+974 99999 9999")
print test

addQatarPrefixToAll(test)
print test