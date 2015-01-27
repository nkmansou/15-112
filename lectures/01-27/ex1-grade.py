# problem: write a program that decides whether or not someone passes the course based on his or her score.

# solution: write a function calculateGrade(grade) that takes a grade as argument
# and returns "pass" or "fail" whether or not the grade is greater than 60% of the maximum score


##### Functions #####

def calculateGrade(grade):
    if grade > (1800*60/100):
        res = " passes the course"
    else:
        res = " fails the course"
    return res

##### My tests #####

# input data

person1 = "Thierry"
grade1 = 800

person2 = "Mohammed"
grade2 = 1702

# calculate the grades
resultOfGrade1 = calculateGrade(grade1)
resultOfGrade2 = calculateGrade(grade2)
result = person1 + resultOfGrade1 + " and " + person2 + resultOfGrade2

# display the result
print "Result is ", result