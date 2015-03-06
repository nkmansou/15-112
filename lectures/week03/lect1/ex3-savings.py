# problem: I have 100,000 QAR on a saving account. Every year my bank gives me 2.5% interest on my savings. In addition, the bank offers me a bonus of 5,000 QAR every 5 years. How much will I have in 10 years? 20 years?

# input data
amount = 100000
interest = 2.5

# calculate interests
for i in range(20):
    amount = amount * 1.025
    if (((i+1) % 5) == 0):
        amount = amount + 5000


# display the result
print "Result is: ", amount