##### Concept of variable #####

quiz = 50
homework = 80
result = (homework + quiz * 2) /2

print "My result is ", result

##### Calculations #####

# problem: convert a temperature from celcius to Farenheit

C = 25
result = C * 9 / 5 + 32

print "My result is ", result

##### Variable and loops #####

# loop 1
result = 0
for i in range(4):
    result = i

print "My result is ", result

# loop 2
result = 0
for i in range(4):
    result = i + result

print "My result is ", result

##### Conditionals #####

# problem: decide wether a number is odd or even

n = 66
if (n%2 == 0):
    result = "even"
else:
    result = "odd"

print "The condition is ", (n%2 == 0)
print "My result is ", result


