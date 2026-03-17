from Class_point import point

class colorpoint(point):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

p1 = colorpoint(0,0,'red')
p2 = colorpoint(10,10,'green')
print(p1.x, p1.y, p1.color)
print(p2.distance_origin())