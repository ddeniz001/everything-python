'''def countLetter(text, letter):
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

print(removeChar("Pig f&ckers for ALabama.", "g"))


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
 
def removeFirstOccurence(string1, string2):
    return 

# 1) Write a function that counts how many non-overlapping /
#    occurences of a substring appear in a string.
def countNonOverlap(s, ss):
    pass    
''' 
'''
# Iteration by position
numbers = [1, 2, 3, 4, 5]
print(numbers)

for i in range(len(numbers)):
    numbers[i] = numbers[i] ** 2

print(numbers)'''
'''
def doubleStuff(lst):
    newlst = []
    for i in range(len(lst)):
        newElem = lst[i] = 2 * lst[i]
        newlst.append(newElem)
    return newlst

arr = [1,2,3,4,5]
print(arr)

print(doubleStuff(arr))
'''
'''
def isPrime(n):
    if n % n == 0:
        return False

def primesUpTo(m):
    result = []
    for i in range(2, m):
        if isPrime(i):
            result.append(i)
        
    return result
'''
'''
def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    print('\t',f)
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True

    
def primesUpTo(n):
    result = [num for num in range(2,n) if is_prime(num)]
    return result

'''


'''
nested = ["hello", 2.0, 5, [10, 20]]
innerlist = nested[3]
print(innerlist)

item = innerlist[1]
print(item)

print(nested[3][1]) 
'''
'''
name = 'Joseph Joestar'
nameList = name.split()
newName = ''

for i in nameList:
    newName += i[0]
    print(newName)
'''
'''
def circleInfo(r):
    a = 2 * 3.14159 * r
    c = 2 * 3.14159 * r
    return (c, a)
'''
'''

import random
aList = []
bList = [1,2,3,4]


def randToList(lst):
    for i in range(1,101):    
        aList.append(random.randint(1, 1001))

    return lst


def getMaxNum(lst):
    maxNum = 0
    for i in lst:
        if i > maxNum:
            maxNum = 0
            maxNum += i
            
    return "Largest number is -->", maxNum 


def getAverage(lst):
    total = 0
    for i in lst:
        total += i
        average = total / len(lst)

    return "The list average is -->", average 


def sumOfSquares(lst):
    squrs = (i**2 for i in lst)
    total = sum(squrs)
    return "Sum of squares is --> ", total


def countOddNumbers(lst):
    count = 0
    for i in lst:
        if i % 2 != 0:
            count +=1
    return count


def sumEvenNums(lst):
    total = 0
    for i in lst:
        if i % 2 == 0:
            total += i
    return "Sum of even numbers -->", total


def sumNegativeNums(lst):
    total = 0
    for i in lst:
        if i < 0:
            total += i
    return total


def sumUpToEven(lst):
    total = 0
    index = 0
   
    while index < len(lst) and index % 2 != 0:
        index +=1
    return total


print(returnSam(cList))
'''

'''
print("1--", randToList(aList))
print("2--", sumOfSquares(bList))
print("3--", getAverage(aList))
print("4--", sumEvenNums(aList))
print("5--", sumUpToEven(aList))'''
'''
def replace(s, old, new):
    newString = ""

    for eachChar in s:
        if eachChar == old:
            s.split(old)
            s.join(new)
            newString = s
    return newString
print(replace("Amanda", "a", "k"))
'''
'''
infile = open("/Users/hoppa/Desktop/qbdata.txt", "r")
outfile = open("qbnames.txt", "w")

line = infile.readline()

while line:
    values = line.split()
    dataline = values[1] + ',' + values[0]
    outfile.write(dataline + "\n")
    line = infile.readline()

infile.close()
outfile.close()
'''
'''
# FIXED
with open("/Users/hoppa/Desktop/studentnames.txt") as f:
    for line in f:
        items = line.split()
        for i in range(len(items[1:])):
            items[i+1] = int(items[i+1])

        average = sum(items[1:]) / len(items[1:])    
        print(items[0], "MAX SCORE->", max(items[1:]), " / MIN SCORE->", min(items[1:]))
        print("---GRADE AVERAGE: ", average,"\n")'''

'''
with open("/Users/hoppa/Desktop/labdata.txt") as f:
    for line in f:
        items = line.split()
        
        for i in range(len(items[:1])):
            xCords = int(items[i])
            print("X:", xCords)
        
        for j in range(len(items[1:])):
            yCords = int(items[i+1])
            print("Y: ", yCords, "\n")       

    def plotRegression(x,y,n):
        m = (sum(x)*sum(y) - n * (x - sum(x)/len(x)*sum(y)/len(y))) / sum(x)**2 - n*x**2
        '''
'''
import turtle
t = turtle.Turtle()
wn = turtle.Screen()
wn.setworldcoordinates(-300,-300,300,300)
with open("/Users/hoppa/Desktop/mystery.txt", "r") as f:
    for line in f:
        items = line.split()
        print(items)
        if items[0] == "UP":
            t.up()
        else:
            if items[0] == "DOWN":
                t.down()
wn.exitonclick()'''


 #  Write a program that allows the user to enter a string. 
 #  It then prints a table of the letters of the alphabet in alphabetical order
 #  which occur in the string together with
 #  the number of times each letter occurs. 
 #  Case should be ignored. 
 #  A sample run of the program might look this this:

'''
d = {'apples': 15, 'bananas': 35, 'grapes': 12}
print(d['bananas'])

d['oranges'] = 20
print(len(d))

def add_fruit(inventory, fruit, quantity=0):
    inventory = {}
    for i in inventory:
        if fruit not in inventory:
            inventory[fruit] = quantity
        else: 
            inventory[fruit] +=1
    return inventory'''


'''
with open("/Users/hoppa/Desktop/alice.txt", "r") as f:
    listing = {}
    longestWord = ""
    for line in f:
        words = line.split()
        for word in words:
            if alphabet in word:
                word.lower()
                if len(word) > len(longestWord):
                    longestWord = word
    print(longestWord)'''


# QUESTION 
'''
1) Modify the recursive tree program using one or all of the following ideas:
2) Modify the thickness of the branches so that as the branchLen gets smaller, the line gets thinner.
3) Modify the color of the branches so that as the branchLengets very short it is colored like a leaf.
4) Modify the angle used in turning the turtle so that at eachbranch point the angle is selected at random in some range. 
        *For example:
            - Choose the angle between 15 and 45 degrees. Play around to see what looks good.
            - Modify the branchLen recursively so that instead of always subtracting 
            the same amount you subtract a random amount in some range.'''

import turtle
import math
'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def getX(self):return self.x    
    def getY(self):return self.y
    def __str__(self):return "x=" + str(self.x) + ", y=" + str(self.y)


    def distanceFromPoint(self, otherPoint):
        dx = (otherPoint.getX() - self.x)
        dy = (otherPoint.getY() - self.y)
        dist = math.sqrt(dx**2 + dy)
        return dist

    def slopeFromOrigin(self):
        if self.x == 0:
            return self.x
        else:
            return self.y / self.x

    def slope(self, anotherPoint):
        if anotherPoint.getX() == self.x:
            return None
        else:
            m = anotherPoint.getY() - self.y/ anotherPoint.getX() - self.x
            return m

    def getLineTo(self, anotherPoint):
        # y = mx + c
        c = -(self.slope(anotherPoint)* self.x - self.y)
        return (self.slope(anotherPoint),c)
        
    def move(self, dx, dy):
        self.x += dx
        self.y += dy 
        
    def distanceFromOrigin(self):
        return ((self.x **2) + (self.y**2))**0.5


    def halfway(self, target):
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return (Point(mx, my))
    
    def reflectX(self):
        nx = self.x
        ny = -self.y
        return (nx, ny)

class Circle:
    def __init__(self,radius):
        self.radius = radius
    
    def getRadius(self):return self.radius

    def findRadius(self):
        r = self.findCircum() / 2 * math.pi
        return r
   
    def findDiameter(self):
        return 2 * self.radius
    
    def findCenter(self):
        return self.findDiameter() / 2

    def findCircum(self):
        return math.pi * self.findDiameter()

    def __str__(self):return str(self.radius)
'''

'''
class Fraction:
    def __init__(self, top,bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return 'Fraction: ' + str(self.num) + "/" + str(self.den)

    def getNum(self):return self.num
    def getDen(self):return self.den
''' 

# testing Git
def test():pass

def breakChocolate(n, m): 
    while n-m != 0:
        ans = n - m

    if n-m <1:
        return 1
    else:
        ans = n-m
        return ans
        
        
