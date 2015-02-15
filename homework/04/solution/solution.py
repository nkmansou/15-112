def someoneSaid(text, name):
    return name + " said \"" + text + "\""

def maxLength(text, max):
    if len(text) > max:
        return text[0:max]
    else:
        return text

def filter(text, word):
    t = " " + text + " "
    w = " " + word + " "
    while w in t:
        i = t.find(w)
        t = t[:i] + "  " + t[i+len(w):]
    return t[1:-1]

def cleaner(text, ab, word):
    t = " " + text + " "
    a = " " + ab + " "
    w = " " + word + " "
    while a in t:
        i = t.find(a)
        t = t[:i] + w + t[i+len(a):]
    return t[1:-1]

def postComment(comment, name):
    comment = filter(comment,"duck")
    comment = filter(comment, "shot")
    comment = cleaner(comment,"u","you")
    comment = cleaner(comment,"r","are")
    comment = cleaner(comment,"4","for")
    comment = cleaner(comment,"1drfl","wonderful")
    comment = cleaner(comment,"LMAO","funny")
    return someoneSaid(maxLength(comment,150),name)

# not using split
def betterComment(comment,name,bads,abs):
    word = ""
    for i in bads:
        if i == " ":
            comment = filter(comment,word)
            word = ""
        else:
            word = word + i
    comment = filter(comment,word)
    word = ""
    for i in abs:
        if i == " ":
            comment = cleaner(comment,word[0:word.find("/")],word[word.find("/")+1:])
            word = ""
        else:
            word = word + i
    comment = cleaner(comment,word[0:word.find("/")],word[word.find("/")+1:])
    return someoneSaid(maxLength(comment,150),name)


# using split
def betterComment(comment,name,bads,abs):
    badList = bads.split(" ")
    for bad in badList:
        comment = filter(comment,bad)
    absList = abs.split(" ")
    for ab in absList:
        words = ab.split("/")
        comment = cleaner(comment,words[0],words[1])
    return someoneSaid(maxLength(comment,150),name)

