class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getVector(self):
        print(self.x, self.y)


myVector = Vector(5, 10)
myVector.getVector()