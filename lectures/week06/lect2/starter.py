# Q1: What is Fahad's revenue?
# Good solution: write a function that takes a seller as argument
# and returns the revenue for this seller

def sellerRevenue(record, months, sellers, name):
   return 0


# Q2: Who is the best seller?
# Good solution: write a function that does not take any argument
# and returns the name of the best seller

def bestSeller(record, months, sellers):
    return ""

# Q3: What was the revenue in February?
# Good solution: write a function that takes a month as argument
# and returns the revenue for this month

def monthRevenue(record, months, sellers, month):
    return ""

# Q4: when was the best month?
# Good solution: write a function that does not take any argument
# and returns the name of the best month

def bestMonth(record, months, sellers):
    return ""

# Q5: what is the total revenue?
# two similar solutions here:
# solution 1: iterate through the sellers and add their revenue
# solution 2: iterate through the months and add their revenue

def total(record, months, sellers):
    return 0

##### Data #####

record = [[0,0,0,0,0,0],[ 456 , 235 , 987 , 673 , 776 , 427], [ 856 , 284 , 413 , 987 , 629 , 196,0 ], [ 198 , 936 , 648 , 925 , 435 , 662,0 ], [174 , 816 , 367 , 357 , 856 , 1045 ]]

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sellers = ["tsans","Fahad", "Emad", "Mariam", "Sarah"]

# print sellerRevenue(record, months, sellers, "Fahad")

print monthRevenue(record, months, sellers,"Apr")