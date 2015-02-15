##### toMinute #####

def toMinutes(hour,minute,am):
    if (hour == 12):
        res = minute
    else:
        res = hour * 60 +  minute
    if not(am):
        res = 12 * 60 + res
    return res

##### length #####

def length(hour1,minute1,am1,hour2,minute2,am2):
    begin = toMinutes(hour1,minute1,am1)
    end = toMinutes(hour2,minute2,am2)
    res = end - begin
    if (res >= 0):
        return res
    else:
        return -1

##### show #####

def show(name,hour1,minute1,am1,hour2,minute2,am2):
    lgh = length(hour1,minute1,am1,hour2,minute2,am2)
    if (lgh < 0):
        result = "time error"
    else:
        result = str(lgh) + " minutes"
    result = name + " (" + result + ")"
    return result





