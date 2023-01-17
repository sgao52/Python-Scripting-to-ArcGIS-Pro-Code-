import math
class River (object):
    def __init__(self, shape):
        self.shape = shape
    def sinuosity(self):
        channel = self.shape.length
        deltaX = self.shape.firstPoint.X - self.shape.lastPoint.X
        deltaY = self.shape.firstPoint.Y - self.shape.lastPoint.Y
        valley = math.sqrt(pow(deltaX, 2) + pow(deltaY, 2))
        return channel/valley
