from abc import ABC, abstractmethod
import math
import matplotlib.pyplot as plt # pip install matplotlib

# see comments at bottom!
class Polygon(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Triangle(Polygon):
    def __init__(self, v1, v2, v3):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
    
    def side_lengths(self):
        a = math.dist(self.v1, self.v2)
        b = math.dist(self.v2, self.v3)
        c = math.dist(self.v3, self.v1)
        return a, b, c
    
    def perimeter(self):
        return sum(self.side_lengths())
    
    def area(self):
        a, b, c = self.side_lengths()
        s = self.perimeter() / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

class RightTriangle(Triangle):
    def __init__(self, v1, v2, v3):
        super().__init__(v1, v2, v3)
        self.is_right()
    
    def is_right(self):
        a, b, c = sorted(self.side_lengths())
        if not math.isclose(a**2 + b**2, c**2):
            raise ValueError("The given vertices do not form a right triangle")

class IsoscelesTriangle(Triangle):
    def __init__(self, v1, v2, v3):
        super().__init__(v1, v2, v3)
        self.is_isosceles()
    
    def is_isosceles(self):
        a, b, c = self.side_lengths()
        if not (math.isclose(a, b) or math.isclose(b, c) or math.isclose(a, c)):
            raise ValueError("The given vertices do not form an isosceles triangle")

# This isn't needed for the assignment but I thought it would be fun anyways ---------------------

def plot_triangle(vertices, title):
    x = [v[0] for v in vertices] + [vertices[0][0]]
    y = [v[1] for v in vertices] + [vertices[0][1]]

    plt.figure()
    plt.plot(x, y, 'bo-')
    plt.fill(x, y, alpha=0.3)
    plt.title(title)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.show()

# User Interactive Code
if __name__ == "__main__":
    try:
        print("Enter the coordinates of three vertices (e.g., 0 0):")
        v1 = tuple(map(float, input("Vertex 1: ").split()))
        v2 = tuple(map(float, input("Vertex 2: ").split()))
        v3 = tuple(map(float, input("Vertex 3: ").split()))

        # Check for Right Triangle
        try:
            triangle = RightTriangle(v1, v2, v3)
            print("This is a Right Triangle.")
            plot_title = "Right Triangle"
        except ValueError:
            # Check for Isosceles Triangle
            try:
                triangle = IsoscelesTriangle(v1, v2, v3)
                print("This is an Isosceles Triangle.")
                plot_title = "Isosceles Triangle"
            except ValueError:
                # Default to Normal Triangle
                triangle = Triangle(v1, v2, v3)
                print("This is a Normal Triangle.")
                plot_title = "Normal Triangle"

        print("Perimeter:", triangle.perimeter())
        print("Area:", triangle.area())

        # (NOT NEEDED FOR CLASS) Plot triangle using matplotlib
        plot_triangle([v1, v2, v3], plot_title)

    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("Unexpected Error:", e)


# Right triangle example:
# 0 0
# 2 0
# 0 2

# Isoscles triangle example:
# 0 0
# 2 0
# 1 2