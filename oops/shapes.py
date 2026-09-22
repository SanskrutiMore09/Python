class Shape():
    def __init__(self , color):
        self.color = color
class Rectangle(Shape):
    def __init__(self,x ,y, width ,height, color):
        super().__init__(color)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def __str__(self):
        return f"x: {self.x} y: {self.y} width: {self.width} height: {self.height}"

rect = Rectangle(x=10, y=20, width=5, height=8, color="blue")

print(rect)
print(f"Area: {rect.get_area()}")
        