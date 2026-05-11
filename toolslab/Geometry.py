import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def expression(self):
        return f"({self.x}, {self.y})"
class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    def length(self, p1, p2):
        return math.sqrt((p2.x-p1.x)**2+(p2.y-p1.y)**2)
class LineString:
    def __init__(self, points):
        self.points = points
    def length(self):
        total = 0
        for i in range(len(self.points)-1):
            total+=math.sqrt((self.points[i+1].x-self.points[i].x)**2+(self.points[i+1].y-self.points[i].y)**2)
        return total
    def size(self):
        return len(self.points)
class Polygon:
    def __init__(self, points):
        self.points = points
    def area(self):
        n = len(self.points)
        if n<3:
            return 0
        s = 0
        for i in range(n):
            x1, y1 = self.points[i].x, self.points[i].y
            x2, y2 = self.points[(i+1)%n].x, self.points[(i+1)%n].y
            s+=x1*y2-x2*y1
        return abs(s)/2
    def circumference(self):
        n = len(self.points)
        if n<2:
            return 0
        elif n==2:
            return math.sqrt((self.points[1].x-self.points[0].x)**2+(self.points[1].y-self.points[0].y)**2)
        C = 0
        for i in range(n):
            p1 = self.points[i]
            p2 = self.points[(i+1)%n]
            C+=math.sqrt((p2.x-p1.x)**2+(p2.y-p1.y)**2)
        return C
