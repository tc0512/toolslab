import math
class Countless: #无数解类
    def __repr__(selt):
        return "Countless"
class Point: #点
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
class Segment: #线段
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    def length(self, p1, p2):
        return math.sqrt((p2.x-p1.x)**2+(p2.y-p1.y)**2)
class Line: #直线
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    def slope(self):
        if self.p1.x==self.p2.x:
            return math.nan()
        return (self.p2.y-self.p1.y)/(self.p2.x-self.p1.x)
    def equation(self):
        if self.p1.x==self.p2.x:
            return f"x={self.p1.x}"
        b = self.p1.y-self.slope()*self.p1.x
        return f"y={self.slope()}x+{b}"
class LineString: #折线
    def __init__(self, points):
        self.points = points
    def length(self):
        total = 0
        for i in range(len(self.points)-1):
            total+=math.sqrt((self.points[i+1].x-self.points[i].x)**2+(self.points[i+1].y-self.points[i].y)**2)
        return total
    def size(self):
        return len(self.points)
class Polygon: #多边形
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
class Box: #矩形
    def __init__(self, ll, ur):
        self.ll = ll
        self.ur = ur
    def __repr__(self):
        return f"Box({self.ll}, {self.ur})"
    def min_corner(self):
        return self.ll
    def max_corner(self):
        return self.ur
    def within(self, p):
        cond1 = (self.ll.x<=p.x and p.x<=self.ur.x)
        cond2 = (self.ll.y<=p.y and p.y<=self.ur.y)
        res = (cond1 and cond2)
        return res
    def width(self):
        return self.ur.x-self.ll.x
    def height(self):
        return self.ur.y-self.ll.y
    def perimeter(self):
        return 2*(self.width()+self.height())
    def area(self):
        return self.width()*self.height()
    def expand(self, p):
        if self.within(p):
            raise ValueError("This point is in the box.")
        elif p.x<=self.ll.x and p.y>=self.ur.y:
            return Box(Point(p.x, self.ll.y), Point(self.ur.x, p.y))
        elif self.ll.x<=p.x and p.x<=self.ur.x and p.y>=self.ur.y:
            return Box(self.ll, Point(self.ur.x, p.y))
        elif p.x>=self.ur.x and p.y>=self.ur.y:
            return Box(self.ll, p)
        elif p.x<=self.ll.x and self.ll.y<=p.y and p.y<=self.ur.y:
            return Box(Point(p.x, self.ll.y), self.ur)
        elif p.x>=self.ll.x and self.ll.y<=p.y and p.y<=self.ur.y:
            return Box(self.ll, Point(p.x, self.ur.y))
        elif p.x<=self.ll.x and p.y<=self.ll.y:
            return Box(p, self.ur)
        elif self.ll.x<=p.x and p.x<=self.ur.x and p.y<=self.ll.y:
            return Box(Point(self.ll.x, p.y), self.ur)
        elif self.ur.x<=p.x and p.y<=self.ll.y:
            return Box(Point(self.ll.x, p.y), Point(p.x, self.ur.y))
        else:
            raise NotImplementedError("Don't implement this situation.")
def _intersection_of_two_lines(l1, l2): #Bug: 字符串未去首
    if "x=" in l1.equation() and "x=" in l2.equation():
        if l1.equation()[2:]==l2.equation()[2:]:
            return Countless()
        return None
    elif "x=" in l1.equation() and "y=" in l2.equation():
        x = float(l1.equation()[2:])
        k, b = l2.equation()[2:].split("x+")
        y = float(k)*x+float(b)
        return Point(x, y)
    elif "y=" in l1.equation() and "x=" in l2.equation():
        x = float(l2.equation()[2:])
        k, b = l1.equation()[2:].split("x+")
        y = float(k)*x+float(b)
        return Point(x, y)
    k1, b1 = l1.equation()[2:].split("x+")
    k2, b2 = l2.equation()[2:].split("x+")
    k1, b1, k2, b2 = float(k1), float(b1), float(k2), float(b2)
    x = (b2-b1)/(k1-k2)
    y = k1*x+b1
    return Point(x, y)
