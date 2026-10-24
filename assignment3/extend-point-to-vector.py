import math

#Task 5

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


class Vector(Point):
    pass

    def __str__(self):
        return f"Vector<{self.x}, {self.y}>"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


point1 = Point(1, 4)
point2 = Point(20, -12)
point3 = Point(1, 4)

print(point1)

print(point1.x)
print(point1.y)

print(point2)

print(point2.x)
print(point2.y)

print(point1 == point2)
print(point1 == point3)

print(point1.distance(point2))

vector1 = Vector(1, 4)
vector2 = Vector(10, 5)

print(vector1)
print(vector2)

print(vector1 == vector2)
print(vector1 + vector2)