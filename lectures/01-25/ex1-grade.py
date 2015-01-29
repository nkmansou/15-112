# problem: write a program that writes "pass" or "fail" whether or not someone passes the course based on his or her score.

# input data
someone = "Thierry"
score = 1653

# calculate the grade
if score > (1700*60/100):
    result = " passes the course "
else:
    result = " fails the course "

result = someone + result + str(score)

# display the result
print "Result is: ", result

print (score > (1700*60/100))