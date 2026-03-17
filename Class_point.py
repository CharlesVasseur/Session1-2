class point:
    def __init__(self, x, y):
        """
        Initialize the point with x,y coordinates
        param x: x coordinate
        param y: y coordinate
        """
        self.x = x
        self.y = y
    def __str__(self):
        """
        Return the string representation of the point
        :return: p<x,y>
        """
        return f"p<{self.x},{self.y}>"
    def __repr__(self):
        return self.__str__()
    def distance_origin(self):
        return (self.x**2 + self.y**2)**0.5
    def __lt__(self, other):
        """
        Compare two points objects
        :param other: the other point object
        :return: bool True or False
        """
        if isinstance(other, int):
            return self.distance_origin() < other
        return self.distance_origin() < other.distance_origin()

if __name__ == '__main__':
    # Instantiate the point class
    p1 = point(1, 2)
    p2 = point(3, 4)
    print(p1.x, p1.y, p2.x, p2.y)
    print(p1, p2)
    p3 = point(4, 3)
    print(p3.distance_origin())
    p4 = point(12, 5)
    print(p4.distance_origin())

    points = [p1, p2, p3, p4, point(-2,6)]
    points.append(point(-5,-5))

    print(points[4].x)
    print(points[5].distance_origin())

    print(points)
    points.sort()
    print(point(7,11).distance_other(point(7,15)))

