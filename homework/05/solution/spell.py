def check(text,words):
    res = []
    chunks = text.split(" ")
    for word in chunks:
        if not(word in words):
            res.append(word)
    return res

def unique(words):
    res = []
    for word in words:
        if not(word in res):
            res.append(word)
    return res

def report(text,words):
    mispellings = check(text,words)
    n = len(mispellings)
    if n == 0:
        return "0 mistake"
    elif n == 1:
        res = "1 mistake: "
    else:
        res = str(n) + " mistakes: "
    for word in unique(mispellings):
        res = res + word + " "
    return res

