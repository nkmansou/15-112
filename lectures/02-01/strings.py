mytext = "Qatar 2022!"

##### string slicing #####

result = mytext[2]

# prints "t"
print "The result is :", result

##### more slicing #####

result = mytext[0:5]

# prints "Qatar"
print "The result is :", result

##### length #####

result = len(mytext)

# prints 11
print "The result is :", result

##### The last character #####

result = mytext[len(mytext)-1]

# prints "!"
print "The result is :", result

# however, python has a predefined instruction to return the last character

result = mytext[-1]

# prints "!"
print "The result is :", result

##### String comparison ######

result = ("hello" == "hello")

# prints True
print "The result is :", result

result = ("hello" == "hello ")

# prints False
print "The result is :", result

result = ("hello" == "Hello")

# prints False
print "The result is :", result

##### in #######

result = ("World Cup" in "Qatar is organizing the 2022 World Cup")

# prints True
print "The result is :", result

result = ("World  Cup" in "Qatar is organizing the 2022 World Cup")

# prints False because there are only space between "World" and  "Cup"
print "The result is :", result

#### Non-mutabillty ####
# strings are non mutable which means that you cannot modify them
# but you can rebuild them

# For instance, in "qatar", we want to change the letter "q" by "Q"

text = "qatar"

# text[0] = "Q" does not work, because you cannot modify the string

# however, you can rebuild a new string
result = "Q" + text[1:len(text)]

# prints "Qatar"
print "The result is :", result







