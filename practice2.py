# 1) Write a function that counts how many non-overlapping /
#    occurences of a substring appear in a string.
def countNonOverlap(s, ss):
    pass    

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
