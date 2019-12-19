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
wn.exitonclick()


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
    return inventory



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
    print(longestWord)