# #### counting #####

def count(text, letter):
    res = 0
    for index in range(len(text)):
        if (text[index] == letter):
            res = res + 1
    return res

## Testing

print count("qatar", "h")
print count("qatar", "t")
print count("qatar", "a")
print count("qatar aaaaaaa!", "a")
print count("qAtar", "a")
print count("", "a")

####### reverse ######

# version 1
def reverse(text):
    res = ""
    for index in range(len(text)):
        res = text[index] + res
    return res

# version 2
def reverse(text):
    res = ""
    for index in range(len(text)):
        res = res + text[len(text)-index-1]
    return res

## Testing

## tests
print reverse("Qatar")
print reverse("racecar")
print reverse("even")
print reverse("")

####### palindrome ######

# version 2
def isPalindrome(text):
    for i in range(len(text)/2):
       if text[i] != text[len(text)-1-i]:
           return False
    return True

# version 1
def isPalindrome(text):
    return (text == reverse(text))

## Testing

print isPalindrome("qatar")
print isPalindrome("racecar")
print isPalindrome("anna")
print isPalindrome("")

####### Word Count ######

def wordCount(text):
    count = 0
    word = False
    for index in range(len(text)):
        if (text[index] == " "):
            word = False
        else:
            if not(word):
                count = count+1
                word = True
    return count

## Testing

print wordCount("")
print wordCount("Qatar")
print wordCount("Qatar is organizing the 2022 World Cup!")
print wordCount("   Qatar  is   organizing the 2022 World  Cup!   ")

####### Common Letters ######

def commonLetters(text1,text2):
   res = ""
   for index in range(len(text1)):
       if (text1[index] in text2) and not(text1[index] in res):
           res = res + text1[index]
   return res

## Testing

print commonLetters("Qatar","Football")
print commonLetters("abcd","abcd")
print commonLetters("aaaa","aaaa")
print commonLetters("abcde","fghi")
print commonLetters("","abcd")

####### Unique Letters ######

def uniqueLetters(text):
   res = ""
   for index in range(len(text)):
       if not(text[index] in res):
           res = res + text[index]
   return res

## Testing

print uniqueLetters("Qatar")
print uniqueLetters("aaaaaa")
print uniqueLetters("bababaaaababbba")
print uniqueLetters("")
print uniqueLetters("abcdef")