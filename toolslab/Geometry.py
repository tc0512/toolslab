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
        for i in range(len(points)-2):
            total+=math.sqrt((points[i+1].x-points[i].x)**2+(points[i+1].y-points[i].y)**2)
        return total
    def size(self):
        return len(points)
