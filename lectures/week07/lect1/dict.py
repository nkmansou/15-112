# a datastructure to record the number of minutes spent exercising each day
# dictionary with keys of type String and values of type int
exercise = {"Sunday": 36, "Monday": 51, "Wednesday": 55, "Thursday": 45}

# print the dictionary
print exercise

# print the number of minutes spent exercising on Wednesday
print exercise["Wednesday"]

# did I exercise on Monday?
print ("Monday" in exercise)

# did I exercise on Tuesday
print ("Tuesday" in exercise)

# insert a new key/value
exercise["Saturday"] = 90
print exercise

# modify an existing key/value pair
exercise["Monday"] = 61
print exercise

# print all keys
for key in exercise:
    print key

# print all values
for key in exercise:
    print exercise[key]

# print all keys and values
for key in exercise:
    print key + ": " + str(exercise[key])




