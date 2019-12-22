import math


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

class labeledPoint(Point):
    def __init__(self, x,y,label):
        self.point = Point(x,y)
        self.label = label

    def __str__(self):
        return "x=" + str(self.x)+", y="+str(self.y)+ " ("+self.label+ ")"

    def distanceFromOrigin(self):
        return self.point.distanceFromOrigin()

lp = labeledPoint(3,4,'a label')

print(lp)



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


# This is a helper function
def gcd(x,y):
    while x % y != 0:
        oldx = x
        oldy = y

        x = oldy
        y = oldx % oldy 
    return y


class Fraction:
    def __init__(self, top,bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return 'Fraction: ' + str(self.num) + " / " + str(self.den)

    def getNum(self):return self.num
    def getDen(self):return self.den

    # This method is a mutator, it changes the state of the object
    def simplify(self):
        common = gcd(self.num, self.den)
        self.num = self.num // common
        self.den = self.den // common

    def add(self, otherFraction):
        newnum = self.num*otherFraction.den + self.den*otherFraction.num
        newden = self.den*otherFraction.getDen
        common = gcd(newden,newnum)
        return Fraction(newnum//common, newden//common)

def rational(f1,f2):
    return f1.getNum() * f2.getDen() == f2.getNum() * f1.getDen()


def breakChocolate(m, n):
    if n*m == 1: return 0
    if (n*m)-1 < 0: return 0
    else:
        return (n*m)-1


def findAverage(r1,r2):return r1 // r2

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getWidth(self):return self.width
    def getheight(self):return self.width

    def __str__(self):
        return "width:"+str(self.width)+"\nheight:"+str(self.height)+"\n"

    def getArea(self):
        return self.width * self.height
    
    def changeDimension(self):
        newheight = int(input("Enter new height: "))
        newWidth = int(input("Enter new Width" ))
        
        newWidth,newheight = self.width,self.height

    def transpose(self):
        newWidth = self.height
        newHeight = self.width
        return Rectangle(newWidth,newHeight)

    def collisionDetection(self):pass

