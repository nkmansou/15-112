###### Currency #####

def toQAR(amount,currency):
    if (currency == "USD"): return (amount * 3.65)
    if (currency == "CNY"): return (amount * 0.57)
    if (currency == "EURO"): return (amount * 4.8)
    
def fromQAR(amount,currency):
    if (currency == "USD"): return (amount / 3.65)
    if (currency == "CNY"): return (amount / 0.57)
    if (currency == "EURO"): return (amount / 4.8)

##### currency tests ######
    
result = "10 QAR is " + str(fromQAR(10, "EURO")) + " EURO (and back " +  str(toQAR(fromQAR(10, "EURO"),"EURO")) + ")\n"
result += "10 QAR is " + str(fromQAR(10, "CYN")) + " CNY (and back " +  str(toQAR(fromQAR(10, "CYN"),"CNY")) + ")\n"
result += "10 QAR is " + str(fromQAR(10, "USD")) + " USD (and back " +  str(toQAR(fromQAR(10, "USD"),"USD")) + ")\n"

print result

###########

###### Ticketing #####

def price(adult, children, membership):
    total = adult * 250
    if children > adult:
        total += adult * 180 * 0.9 + (children - adult) * 180
    else:
         total += children * 180 * 0.9
    return (total - 20 * membership)

##### ticketing tests ######
    
result  = "price(2,4,2) is " + str(price(2,4,2)) + "\n" 
result += "price(2,1,0) is " + str(price(2,1,0)) + "\n" 
result += "price(2,2,0) is " + str(price(2,2,0)) + "\n" 

print result

###########

###### Headlines #####

def headline(team1,score1,team2,score2):
    if (score1 > score2):
        return team1 + " won against " + team2 + " ("+ str(score1) + "," + str(score2) + ")" 
    elif (score1 == score2):
        return team1 + " tied " + team2 + " ("+ str(score1) + "," + str(score2) + ")" 
    else:
        return team1 + " lost against " + team2 + " ("+ str(score1) + "," + str(score2) + ")"
             
 ##### headlines tests ######

result  = headline("Qatar",3,"England",2)
result += headline("Italy",2,"France",2)
result += headline("Germany",0,"Brazil",2)

print result

###########

###### checksum #####

def checksum(ticket):
    sum = 0
    i = 1
    while(ticket > 0):
        sum += ticket % (10 * i)
        ticket = (ticket / 10)
    return ((sum % 11) == 0)
        
def ticketGenerator(upper, lower):
    tickets = ""
    for i in range(upper,lower):
        if checksum(i):
            tickets += " " + str(i)
    return tickets
             
 ##### headlines tests ######

result  = ticketGenerator(1000,2000)
print result

###########


print "Exercise 1"
print "10 QAR is " + str(fromQAR(10, "EURO")) + " EURO (and back " +  str(toQAR(fromQAR(10, "EURO"),"EURO")) + ")"
print "10 QAR is " + str(fromQAR(10, "CNY")) + " CNY (and back " +  str(toQAR(fromQAR(10, "CNY"),"CNY")) + ")"
print "10 QAR is " + str(fromQAR(10, "USD")) + " USD (and back " +  str(toQAR(fromQAR(10, "USD"),"USD")) + ")"

print "\n Exercise 2"
test1 = price(2,4,2)
test2 = price(2,1,0)
test3 = price(2,2,0)

print  str(test1 == 1012.0) + " (" + str(test1) + ")"
print  str(test2 == 626.0) + " (" + str(test2) + ")"
print  str(test3 == 752.0) + " (" + str(test3) + ")"


print "\n Exercise 3"

test1 = headline("Qatar",3,"England",2)
test2= headline("Italy",2,"France",2)
test3 = headline("Germany",0,"Brazil",2)

print  str(test1 == "Qatar won against England (3,2)") + " (" + str(test1) + ")"
print  str(test2 == "Italy tied France (2,2)") + " (" + str(test2) + ")"
print  str(test3 == "Germany lost against Brazil (0,2)") + " (" + str(test3) + ")"

print "\n Exercise4"

test = ticketGenerator(1000,2000)

print  str(test == " 1019 1028 1037 1046 1055 1064 1073 1082 1091 1109 1118 1127 1136 1145 1154 1163 1172 1181 1190 1208 1217 1226 1235 1244 1253 1262 1271 1280 1307 1316 1325 1334 1343 1352 1361 1370 1399 1406 1415 1424 1433 1442 1451 1460 1489 1498 1505 1514 1523 1532 1541 1550 1579 1588 1597 1604 1613 1622 1631 1640 1669 1678 1687 1696 1703 1712 1721 1730 1759 1768 1777 1786 1795 1802 1811 1820 1849 1858 1867 1876 1885 1894 1901 1910 1939 1948 1957 1966 1975 1984 1993") + " (" + str(test) + ")"
