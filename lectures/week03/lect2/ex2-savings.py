# problem: I have 100,000 QAR on a saving account. Every year my bank gives me 2.5% interest on my savings. In addition, the bank offers me a bonus of 5,000 QAR every 5 years. How much will I have in 10 years? 20 years?

##### Functions #####

def calculateCompoundInterest(amount,interest,years, bonus):
    for i in range(years):
        amount = amount * (1 + interest/100.0)
    if bonus:
        amount = amount + 5000 * (years/5)
    return amount

##### My tests #####

amount = calculateCompoundInterest(10000,3,8,True)
print "Your revenue is " + str(amount)
print calculateCompoundInterest(2023,7.6, 5, False)
print calculateCompoundInterest(10,0.5,20, False)
print calculateCompoundInterest(7893548,3,16, True)

