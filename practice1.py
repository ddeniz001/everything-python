def countLetter(text, letter):
    counter = 0
    for eachChar in text:
        if eachChar == letter:
            counter += 1
    return counter


def find(astring, achar):
    ix = 0
    found = False

    while ix < len(astring):
        if astring[ix] == achar:
            found = True
        if not found:
            ix += 1
        if found:
            return True
        else:
            return -1


def find4(astring, achar, start=0, end=None):
    
    ix = start
    if end == None:
        end = len(astring)

    found = False
    while ix < end and not found:
        if astring[ix] == achar:
            found = True
        else:
            ix = ix + 1
    if found:
        return ix
    else:
        return -1

ss = "Python strings have some interesting methods."
            
print(find4(ss, "s"))
print(find4(ss, 's', 7))
print(find4(ss, 's', 8))
print(find4(ss, 's', 8, 13))
print(find4(ss, '.'))


prefixes = "JKLMNOPQ"
suffix = "ack"

for p in prefixes:
    if p == "O" or p == "Q":
        print(p + "u" + suffix)

    print(p + suffix)
'''

'''
def find_e(text):
    lows = "abcdefghijklmnopqrstuvwxyz"
    ups = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    total_e = 0
    totalChars = 0

    for achar in text:
        if achar in lows or achar in ups:
            totalChars+=1
            if achar == 'e':
                total_e +=1
    
    percentage = ((total_e / totalChars) * 100)
    print("Your text contains a total of -> ", totalChars," alphabetic characters of which ", total_e, "(", percentage,"%) are 'e'.")
           
quote = "It's like everyone tells a story about themselves inside their own head."

find_e(quote)
'''
'''
def findDigit(number):
    number_str = str(number)
    return len(number_str)


findDigit(400)

def mirrorString(s):
    return (s[::-1], s)
print(mirrorString("baba"))


# Strings are immutable, so you have to create a new string
def removeChar(text, char):
    newString = ""
    for i in text:
        if i != char:
            newString += i
    return newString

print(removeChar("Pig f&ckers for ALAbama.", "g"))

def borrow(s):
    punctuations = '''!()-[];:'"{\,<>./?@}#$%^&*_~'''
    newstr = ""

    for char in s:
        if char not in punctuations:
            newstr+=char
            newstr = newstr.replace(' ','').lower()

    return newstr

print(borrow('aNnA liveS!!!!'))

def reversed(mystr):
    reversedStr = ""
    for i in mystr:
        reversedStr += i
    return reversedStr

def isPalindrome(myStr):
    if myStr in reversed(myStr):
        return True
    else:
        return False
 
def removeFirstOccurence(string1, word):return 
