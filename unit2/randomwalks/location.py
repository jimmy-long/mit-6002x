class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX,
                        self.y + deltaY)

    def distFrom(self, other):
        ox = other.getX()
        oy = other.getY()
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist**2 + yDist**2)**0.5 #Pythag theorem

    def getX(self):
        return self.x

    def getY(self):
        return self.y

