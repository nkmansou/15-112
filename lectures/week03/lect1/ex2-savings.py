# problem: I have 100,000 QAR on a saving account. Every year my bank gives me 2.5% interest on my savings. How much money will I have in 10 years? 20 years?

# input data
amount = 100000
interest = 2.5

# calculate interests
for i in range(5):
    amount = amount * 1.025

# display the result
print "Result is: ", amount



