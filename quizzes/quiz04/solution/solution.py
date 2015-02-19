def analyze(text):
    res = ""
    nbspace = 0
    nbletter = 0
    for i in range(len(text)):
        if text[i] == ".":
            res = res + ". [space:" + str(nbspace) + ", letter:" + str(nbletter) + "] "
            nbspace = 0
            nbletter = 0
        elif text[i] == " ":
            res = res + " "
            nbspace = nbspace + 1
        else:
            res = res + text[i]
            nbletter = nbletter + 1
    return res