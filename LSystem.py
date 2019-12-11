import turtle


'''
def drawSquare(t, sz):
    for i in range(3):
        t.forward(sz)
        t.left(120)


tess = turtle.Turtle()
wn = turtle.Screen()
drawSquare(tess, 60)

wn.exitonclick()'''


'''def removeVowels(s):
    vowels = "aeiouAEIOU"
    strWithoutVowels = ""
    for char in s:
        if char not in vowels:
            strWithoutVowels += char
    
    return strWithoutVowels'''


'''------------------------------------

def applyRules(ch):
    newStr = ""
    if ch == 'F':
        newStr = 'F-F++F-F'
    else:
        newStr = ch
    
    return newStr


def processString(oldStr):
    newstr = ""
    for char in oldStr:
        newstr += applyRules(char)

    return newstr
    

def createLSystem(numIters, axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString += processString(startString)
        startString = endString
    
    return endString
  
def drawLsystem(aTurtle, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)

def main():
    inst = createLSystem(4, "F")
    print(inst)
    t = turtle.Turtle()
    wn = turtle.Screen()

    t.up()
    t.back(200)
    t.down()
'''


def createLSystem(numIters, axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString += processString(startString)
        startString = endString
    
    return endString


def applyRules(ch):
    newStr = ""
    if ch == 'L':
        newStr = '+RF-LFL-FR+'
    if ch == 'R':
        newStr = '-LF+RFR+FL-'
    else:
        newStr = ch
    
    return newStr



def processString(oldStr):
    newstr = ""
    for char in oldStr:
        newstr += applyRules(char)

    return newstr
    

  
def drawLsystem(aTurtle, instructions, angle, distance):
    savedInfo = []
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)
        elif cmd == '[':
            savedInfo.append(aTurtle.heading(), aTurtle.xcor, aTurtle.ycor)
        elif cmd == ']':
            newInfo = savedInfo.pop()
            print(newInfo)
            print(savedInfo)


def main():
    inst = createLSystem(4, "R")
    print(inst)
    t = turtle.Turtle()
    wn = turtle.Screen()

    t.up()
    t.back(250)
    t.down()
    drawLsystem(t, inst, 90, 6)

    wn.exitonclick()


main()

