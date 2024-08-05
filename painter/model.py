# TODO: Add code here

import matplotlib.pyplot as plt

class Point:
    def _init_(self, x: float, y: float):
        self.x = x
        self.y = y

class Circle:
    def _init_(self, center: Point, radius: float):
        self.center = center
        self.radius = radius

    def area(self) -> float:
        return 3.14159 * self.radius ** 2

    def draw(self):
        circle = plt.Circle((self.center.x, self.center.y), self.radius, color='r')
        plt.gca().add_patch(circle)
        plt.axis('scaled')
        plt.show()

    def _str_(self):
        return f'circle with center at ({self.center.x}, {self.center.y}) and radius {self.radius}'

class Triangle:
    def _init_(self, point1: Point, point2: Point, point3: Point):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

    def area(self) -> float:
        return abs(
            (self.point1.x * (self.point2.y - self.point3.y) +
             self.point2.x * (self.point3.y - self.point1.y) +
             self.point3.x * (self.point1.y - self.point2.y)) / 2
        )

    def draw(self):
        x = [self.point1.x, self.point2.x, self.point3.x, self.point1.x]
        y = [self.point1.y, self.point2.y, self.point3.y, self.point1.y]
        plt.fill(x, y, color='b')
        plt.axis('scaled')
        plt.show()

    def _str_(self):
        return f'Triangle with vertices at ({self.point1.x}, {self.point1.y}), ' \
               f'({self.point2.x}, {self.point2.y}), ({self.point3.x}, {self.point3.y})'

class Rectangle:
    def _init_(self, point1: Point, point2: Point):
        self.point1 = point1
        self.point2 = point2

    def area(self) -> float:
        width = abs(self.point2.x - self.point1.x)
        height = abs(self.point2.y - self.point1.y)
        return width * height

    def draw(self):
        x = [self.point1.x, self.point2.x, self.point2.x, self.point1.x, self.point1.x]
        y = [self.point1.y, self.point1.y, self.point2.y, self.point2.y, self.point1.y]
        plt.fill(x, y, color='g')
        plt.axis('scaled')
        plt.show()

    def _str_(self):
        return f'Rectangle with vertices at ({self.point1.x}, {self.point1.y}) and ' \
               f'({self.point2.x}, {self.point2.y})'