def add(numbers):
    res = 0
    for n in numbers:
        res = res + n
    return res

print add([23,56,936, 767])

def glue(words):
    res = ""
    for word in words:
        res = res + word + " "
    return res

print glue(["This", "is", "easy","!"])

def abs(numbers):
    result = []
    for n in range(len(numbers)):
        if numbers[n]<0:
            result.append(-numbers[n])
        else:
            result.append(numbers[n])
    return result

print abs([2,-6,31,-99])

def negativeValues(numbers):
    result = []
    for n in range(len(numbers)):
        if numbers[n]>=0:
            result.append(numbers[n])
    return result

print negativeValues([2,-6,31,-99])

