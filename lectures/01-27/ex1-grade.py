# problem: write a program that decides whether or not someone passes the course based on his or her score.

# solution: write a function calculateGrade(grade) that takes a grade as argument
# and returns "pass" or "fail" whether or not the grade is greater than 60% of the maximum score


##### Functions #####

def calculateGrade(grade):
    percent = grade / 1700.0 * 100
    return "Your percentage is " + str(percent) + "%"

##### My tests #####

# input data

person1 = "Thierry"
grade1 = 1600

# calculate the grades
print calculateGrade(grade1)