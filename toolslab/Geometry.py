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
class Line: #直线
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    def slope(self):
        if self.p1.x==self.p2.x:
            return math.nan()
        return (self.p2.y-self.p1.y)/(self.p2.x-self.p1.x)
    def equation(self):
        A = self.p1.y-self.p2.y
        B = self.p2.x-self.p1.x
        C = self.p1.x*self.p2.y-self.p2.x*self.p1.y
        return [A, B, C]
    def directional_vector(self):
        return (self.p2.x-self.p1.x, self.p2.y-self.p1.y)
class Segment: #线段
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    def length(self, p1, p2):
        return math.sqrt((p2.x-p1.x)**2+(p2.y-p1.y)**2)
    def start(self):
        return self.p1
    def end(self):
        return self.p2
    def line(self):
        return Line(self.p1, self.p2).equation()
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
def _intersection_of_two_lines(l1, l2): #private function: 两线交点
    A1, B1, C1 = l1.equation()
    A2, B2, C2 = l2.equation()
    delta = A1*B2-A2*B1
    if delta==0:
        if A1*C2-A2*C1!=0 or B1*C2-B2*C1!=0:
            return None
        elif A1*C2-A2*C1==0 and B1*C2-B2*C1==0:
            return Countless()
    x, y = (B1*C2-B2*C1)/delta, (C1*A2-C2*A1)/delta
    return Point(x, y)
def _is_on_segment(point, seg_p1, seg_p2): #private function：点是否在线段上
    x, y = point.x, point.y
    x1, y1 = seg_p1.x, seg_p1.y
    x2, y2 = seg_p2.x, seg_p2.y
    return (min(x1, x2)<=x<=max(x1, x2) and min(y1, y2)<=y<= max(y1, y2))
def _intersection_of_line_and_seg(l, seg): #private function：直线与线段交点
    point = _intersection_of_two_lines(line, segment.line)
    if point is None or isinstance(point, Countless):
        return point
    if _is_on_segment(point, segment.p1, segment.p2):
        return point
    return None
def _intersection_of_line_and_polygon(l, poly): #private function：直线与多边形交点
    a, b, c = l.equation()
    if abs(b)>0:
        O = Point(0, -c/b)
    elif abs(a)>0:
        O = Point(-c/a, 0)
    else:
        O = Point(0, 0)
    D = l.directional_vector()
    intersections = []
    polygon = poly.points
    n = len(polygon)
    for i in range(n):
        A = polygon[i]
        B = polygon[(i+1)%n]
        dx = B.x-A.x
        dy = B.y-A.y
        denom = D[0]*dy-D[1]*dx
        if abs(denom)==0:
            continue
        t = ((A.x-O.x)*dy-(A.y-O.y)*dx)/denom
        s = ((A.x-O.x)*D[1]-(A.y-O.y)*D[0])/denom
        if 0 <= s <= 1:
            x = O.x+t*D[0]
            y = O.y+t*D[1]
            intersections.append(Point(x, y))
    unique = []
    for p in intersections:
        if not any(abs(p.x-q.x)==0 and abs(p.y-q.y)==0 for q in unique):
            unique.append(p)
    return unique
def _intersection_of_seg_and_polygon(seg, poly): #private function: 线段与多边形交点
    A_seg = seg.start()
    B_seg = seg.end()
    D = (B_seg.x-A_seg.x, B_seg.y-A_seg.y)
    O = A_seg
    intersections = []
    polygon = poly.points
    n = len(polygon)
    for i in range(n):
        A = polygon[i]
        B = polygon[(i+1)%n]
        dx = B.x-A.x
        dy = B.y-A.y
        denom = D[0]*dy-D[1]*dx
        if abs(denom)==0:
            continue
        t = ((A.x-O.x)*dy-(A.y-O.y)*dx)/denom
        s = ((A.x-O.x)*D[1]-(A.y-O.y)*D[0])/denom
        if 0<=s<=1 and 0<=t<=1:
            x = O.x+t*D[0]
            y = O.y+t*D[1]
            intersections.append(Point(x, y))
    unique = []
    for p in intersections:
        if not any(abs(p.x-q.x)==0 and abs(p.y-q.y)==0 for q in unique):
            unique.append(p)
    return unique
def intersection(a, b): #交点
    # 两条直线
    if isinstance(a, Line) and isinstance(b, Line):
        return _intersection_of_two_lines(a, b)
    # 直线和线段
    if isinstance(a, Line) and isinstance(b, Segment):
        return _intersection_of_line_and_seg(a, b)
    if isinstance(a, Segment) and isinstance(b, Line):
        return _intersection_of_line_and_seg(b, a)
    # 直线和多边形
    if isinstance(a, Line) and isinstance(b, Polygon):
        return _intersection_of_line_and_polygon(a, b)
    if isinstance(a, Polygon) and isinstance(b, Line):
        return _intersection_of_line_and_polygon(b, a)
    # 线段和多边形
    if isinstance(a, Segment) and instance(b, Polygon):
        return _intersection_of_seg_and_polygon(a, b)
    if isinstance(a, Polygon) and instance(b, Segment):
        return _intersection_of_seg_and_polygon(b, a)
    raise NotImplementedError("Sorry, we donot support this situation.")
